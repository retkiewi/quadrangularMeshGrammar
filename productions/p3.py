import networkx as nx
from productions.decorators import first_isomorphism
from typing import Dict
import operator


class P3():
    left = nx.Graph()
    left.add_node(1, label='I')
    
    for i in range(2, 6):
        left.add_node(i, label='E')
    
    # connect middle to the edges
    left.add_edges_from([(1, i) for i in range(2, 6)])
    
    # cycle between edge nodes
    left.add_edges_from([(i, (i-1)%4 + 2) for i in range(2, 6)])

    @staticmethod
    @first_isomorphism(left)
    def apply(G: nx.Graph, isomorphism: Dict = None):
        if isomorphism is None:
            return False

        nodes_in_G = list(isomorphism.keys())

        # variables
        I_node = None
        layer = None
        prev_I_node = None
        [origin, bound] = None, None
        origin_x, origin_y, bound_x, bound_y = None, None, None, None
        nodes_count = G.number_of_nodes()
        
        # utility functions
        def add_next_layer_node(label, pos):
            nonlocal nodes_count
            nodes_count += 1
            G.add_node(nodes_count, label=label, pos=pos, layer=layer+1)
            return nodes_count

        # Get data from graph
        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'I':
                I_node = G.nodes[node]
                layer = I_node['layer']
                I_node['label'] = 'i'
                prev_I_node = node
            else:
                origin = min(origin, G.nodes[node]['pos']) if origin is not None else G.nodes[node]['pos']
                bound = max(bound, G.nodes[node]['pos']) if bound is not None else G.nodes[node]['pos']

        dimensions = [bound[i] - origin[i] for i in range(2)]

        new_I_nodes = []
        # Add middle nodes
        for k in range(4):
            
            # calculate indecies 
            indecies = [2*(k % 2) + 1, 2*(k // 2) + 1]
            
            size = 4
            
            # calculate position
            position = [origin[i] + dimensions[i]*indecies[i]/size for i in range(2)]
            
            s = add_next_layer_node('I', position)
            new_I_nodes.append(s)
            
            # Add edge between middle nodes and previous middle node
            G.add_edge(s, prev_I_node)
            
        new_E_nodes = []
        # Add edge nodes
        for k in range(9):
            
            # calculate indecies
            indecies = [k % 3, k // 3]
            
            size = 2
            
            # calculate position
            position = [origin[i] + dimensions[i]*indecies[i]/size for i in range(2)]

            s = add_next_layer_node('E', position)
            new_E_nodes.append(s)
        
        # matrix of indecies of nodes connected to each middle node
        indecies_matrix = [[0, 1, 3, 4]]
        while len(indecies_matrix) < 4:
            first = indecies_matrix[0]
            addition = first[len(indecies_matrix)]
            indecies_matrix.append([j + addition for j in first]) 
             
        # Add edges between edge nodes and middle nodes           
        for k,indecies in enumerate(indecies_matrix):
            current_I_node = new_I_nodes[k]
            #get E nodes from indecies
            current_E_nodes = [new_E_nodes[i] for i in indecies]
            G.add_edges_from([(current_I_node, node) for node in current_E_nodes])

        # Add horizontal edges between edge nodes
        for k in range(3):
            i = 3*k+1
            start_E_node = new_E_nodes[i]
            end_E_nodes = [new_E_nodes[j] for j in [i+1, i-1]]
            
            G.add_edges_from([(start_E_node, node) for node in end_E_nodes])
        
        # Add vertical edges between edge nodes 
        for k in range(3):
            i = 3+k
            start_E_node = new_E_nodes[i]
            end_E_nodes = [new_E_nodes[j] for j in [i+3, i-3]]
            
            G.add_edges_from([(start_E_node, node) for node in end_E_nodes])

        return True
