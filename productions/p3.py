import networkx as nx
from productions.decorators import first_isomorphism
from typing import Dict
import operator


class P3():
    left = nx.Graph()
    
    for i in range(1, 5):
        left.add_node(i, label='E')
        
    left.add_node(6, label='I')
    
    # connect middle to the edges
    left.add_edges_from([(6, i) for i in range(1, 5)])
    
    # cycle between edge nodes
    left.add_edges_from([(i, (i%4)+1) for i in range(1, 5)])

    @staticmethod
    @first_isomorphism(left)
    def apply(G: nx.Graph, isomorphism: Dict = None):
        if isomorphism is None:
            print('No isomorphisms found')
            return False

        # variables
        origin_E_node = None
        prev_I_node = None
        layer = None
        edge_vectors = [None, None]
        nodes_count = None
        
        # utility functions
        def add_next_layer_node(label, pos):
            nonlocal nodes_count
            nodes_count += 1
            G.add_node(nodes_count, label=label, pos=pos, layer=layer+1)
            return nodes_count
        
        def split_based_on_label(nodes_in_G):
            E_nodes, I_node = [], []
            [(E_nodes, I_node)[G.nodes[node]['label'] == 'I'].append(node) for node in nodes_in_G]
            return E_nodes, I_node
        
        def calculate_edge_vectors(origin_node):
            neighbor_nodes = [node for node in list(G.neighbors(origin_node)) if G.nodes[node]['label'] == 'E']
            edge_vectors = [
                [node['pos'][j] - G.nodes[origin_node]['pos'][j] for j in range(2)] 
                for node in [G.nodes[node] for node in neighbor_nodes]
            ]
            
            return edge_vectors
        
        def assign_variables(debug=False):
            nonlocal origin_E_node, prev_I_node, layer, edge_vectors, nodes_count
            prev_E_nodes, [prev_I_node] = split_based_on_label(list(isomorphism.keys()))
            layer = G.nodes[prev_I_node]['layer']
            origin_index = prev_E_nodes[0]
            origin_E_node = G.nodes[origin_index]
            edge_vectors = calculate_edge_vectors(origin_index)
            nodes_count = G.number_of_nodes()
            if debug:
                print('prev_E_nodes:', prev_E_nodes)
                print('prev_I_node: ', prev_I_node)
                print('layer:       ', layer)
                print('edge_vectors:', edge_vectors)
                print('nodes_count: ', nodes_count)
                
        def update_prev_I_node():
            nonlocal prev_I_node
            G.nodes[prev_I_node]['label'] = 'i'
          
        def calculate_indecies(k, count, line_length, offset_x, offset_y):
            multiplier_x = (1-2*offset_x)/(line_length-1)
            multiplier_y = (1-2*offset_y)/(count//line_length-1)
            
            return [
                multiplier_x*(k % line_length) + offset_x,
                multiplier_y*(k // line_length) + offset_y
            ]
            
        def calculate_position(ind):
            new_pos = [x for x in origin_E_node['pos']]
            for j in range(2):
                new_pos = [new_pos[i] + edge_vectors[j][i]*ind[j] for i in range(2)]
            return new_pos  
        
        def general_add_new_nodes(label, count, line_length, offset_x, offset_y=None, debug=False):
            new_nodes = []
            for k in range(count):
                indecies = calculate_indecies(k, count, line_length, offset_x, offset_y if offset_y else offset_x)
                position = calculate_position(indecies)
            
                s = add_next_layer_node(label, position)
                new_nodes.append(s)
                if debug:
                    print(f'********** k={k} **********')
                    print('indecies:', indecies)
                    print('position:', position)
            return new_nodes
                
        def add_new_I_nodes(debug=False):
            return general_add_new_nodes(
                label='I', 
                count=4, 
                line_length=2, 
                offset_x=1./4, 
                debug=debug
            )
        
        def connect_I_nodes(I_nodes):
            # Add edge between middle nodes and previous middle node
            [G.add_edge(s, prev_I_node) for s in I_nodes]
    
        def add_new_E_nodes(debug=False):
            return general_add_new_nodes(
                label='E',
                count=9,
                line_length=3,
                offset_x=0,
                debug=debug
            )
        
        def connect_E_nodes(E_nodes, I_nodes):
            # Add edges between middle nodes closest edge nodes
            indecies_matrix = [[0, 1, 3, 4], [1, 2, 4, 5], [3, 4, 6, 7], [4, 5, 7, 8]]
            for k, indecies in enumerate(indecies_matrix):
                I_node = I_nodes[k]
                [G.add_edge(I_node, node) for node in [E_nodes[i] for i in indecies]]
            
            # Add horizontal edges between edge nodes
            for k in range(3):
                E_node = E_nodes[(3*k + 1)]
                indecies = [(3*k + 1) + i for i in [-1, 1]]
                [G.add_edge(E_node, node) for node in [E_nodes[i] for i in indecies]]
            
            # Add vertical edges between edge nodes
            for k in range(3):
                E_node = E_nodes[(k+3)]
                indecies = [(k+3) + 3*i for i in [-1, 1]]
                [G.add_edge(E_node, node) for node in [E_nodes[i] for i in indecies]]
        
        
        
        # main function
        assign_variables()
        update_prev_I_node()
        
        new_I_nodes = add_new_I_nodes()
        connect_I_nodes(new_I_nodes)
        
        new_E_nodes = add_new_E_nodes()
        connect_E_nodes(new_E_nodes, new_I_nodes)

        return True
