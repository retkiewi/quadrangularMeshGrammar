import networkx as nx
from productions.decorators import all_isomorphisms, first_isomorphism
from typing import Dict


class P4():
    left = nx.Graph()
    left.add_node(1, label='I')
    left.add_node(2, label='E')    
    left.add_node(3, label='E')
    left.add_node(4, label='E')
    left.add_node(5, label='E')
    left.add_node(6, label='E')
    

    # connect middle to the edges
    left.add_edges_from([(1, i) for i in range(2, 6)])
    
    # edge nodes
    left.add_edge(2, 6)
    left.add_edge(6, 3)
    left.add_edge(3, 5)
    left.add_edge(5, 4)
    left.add_edge(4, 2)  


    #TODO: add decorator for checking grammar predicate (5th edge node is evenly distanced from the two closest nodes)
    @staticmethod
    @all_isomorphisms(left)
    def apply(G: nx.Graph, offset=1, isomorphisms: list[Dict] = []):
        if len(isomorphisms) == 0:
            print('No isomorphisms found')
            return False

        # variables
        I_node = None
        layer = None
        prev_I_node = None
        [origin, bound] = None, None
        origin_x, origin_y, bound_x, bound_y = None, None, None, None
        nodes_count = G.number_of_nodes()
        vertical = True
        isomorphism = None
        
        for isomorphism_candidate in isomorphisms:
            nodes = list(isomorphism_candidate.keys())

            for node in nodes:
                neighbors = list(G.neighbors(node))
                if len(neighbors) == 2:
                    avg_pos = []
                    for neighbor in neighbors:
                        avg_pos.append(G.nodes[neighbor]['pos'])
                        
                    vertical = avg_pos[0][1] == avg_pos[1][1]

                    avg_pos = [sum(x)/len(x) for x in zip(*avg_pos)]
                
                    if G.nodes[node]['pos'][0] == avg_pos[0] and G.nodes[node]['pos'][1] == avg_pos[1]:
                        isomorphism = isomorphism_candidate                        
                        break                    
                                                


        if isomorphism is None:
            print('No isomorphism found')
            return False

        nodes_in_G = list(isomorphism.keys())

        
        
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
        for k in range(2):
            
            # calculate indecies 
            indecies = [2*k + 1, 1] if vertical else [1, 2*k + 1]
            
            size = [4, 2] if vertical else [2, 4]
            
            # calculate position
            position = [origin[i] + dimensions[i]*indecies[i]/size[i] for i in range(2)]
            
            s = add_next_layer_node('I', position)
            new_I_nodes.append(s)
            
            # Add edge between middle nodes and previous middle node
            G.add_edge(s, prev_I_node)
            
        new_E_nodes = []
        # Add edge nodes
        for k in range(6):
            
            # calculate indecies
            indecies = [k % 3, k // 3] if vertical else [k % 2, k // 2]
            
            size = [2, 1] if vertical else [1, 2]
            
            # calculate position
            position = [origin[i] + dimensions[i]*indecies[i]/size[i] for i in range(2)]
            print(k, position)

            s = add_next_layer_node('E', position)
            new_E_nodes.append(s)
        
        # matrix of indecies of nodes connected to each middle node
        indecies_matrix = [[0, 1, 3, 4]] if vertical else [[0, 2, 1, 3]]
        while len(indecies_matrix) < 2:
            first = indecies_matrix[0]
            addition = first[len(indecies_matrix)]
            indecies_matrix.append([j + addition for j in first]) 
             
        # Add edges between edge nodes and middle nodes           
        for k,indecies in enumerate(indecies_matrix):
            current_I_node = new_I_nodes[k]
            #get E nodes from indecies
            current_E_nodes = [new_E_nodes[i] for i in indecies]
            print(current_E_nodes, current_I_node)
            G.add_edges_from([(current_I_node, node) for node in current_E_nodes])

        # Add horizontal edges between edge nodes
        for k in range(2 if vertical else 3):
            i = 3*k+1 if vertical else 2*k+1
            start_E_node = new_E_nodes[i]
            end_E_nodes = [new_E_nodes[j] for j in ([i+1, i-1] if vertical else [i-1])]
            
            G.add_edges_from([(start_E_node, node) for node in end_E_nodes])
        
        # Add vertical edges between edge nodes 
        for k in range(3 if vertical else 2):
            i = 3+k if vertical else 2+k
            start_E_node = new_E_nodes[i]
            end_E_nodes = [new_E_nodes[j] for j in ([i-3] if vertical else [i-2, i+2])]
            
            G.add_edges_from([(start_E_node, node) for node in end_E_nodes])

        return True
