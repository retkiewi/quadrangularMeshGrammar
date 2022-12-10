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

        # variables
        prev_nodes_E = []
        prev_node_I = None
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
            nodes_E, node_I = [], []
            [(nodes_E, node_I)[G.nodes[node]['label'] == 'I'].append(node) for node in nodes_in_G]
            return nodes_E, node_I
        
        def calculate_edge_vectors(nodes_E):
            origin_node = G.nodes[nodes_E[0]]
            edge_vectors = [
                [node['pos'][j] - origin_node['pos'][j] for j in range(2)] 
                for node in [G.nodes[nodes_E[i]] for i in range(1,4)]
            ]
            # add all vectors
            v_sum = [sum([vector[i] for vector in edge_vectors]) for i in range(2)]
            for vector in edge_vectors:
                if all([True if v_sum[i] == 2*vector[i] else False for i in range(2)]):
                    edge_vectors.remove(vector) 
            
            return edge_vectors
        
        def assign_variables(debug=False):
            nonlocal prev_nodes_E, prev_node_I, layer, edge_vectors, nodes_count
            prev_nodes_E, [prev_node_I] = split_based_on_label(list(isomorphism.keys()))
            layer = G.nodes[prev_node_I]['layer']
            edge_vectors = calculate_edge_vectors(prev_nodes_E)
            nodes_count = G.number_of_nodes()
            if debug:
                print('prev_nodes_E:', prev_nodes_E)
                print('prev_node_I: ', prev_node_I)
                print('layer:       ', layer)
                print('edge_vectors:', edge_vectors)
                print('nodes_count: ', nodes_count)
                
        def update_prev_node_I():
            nonlocal prev_node_I
            G.nodes[prev_node_I]['label'] = 'i'
          
        def calculate_indecies(k, line_length, offset):
            multiplier = (1-2*offset)/(line_length-1)
            return [
                multiplier*(k % line_length) + offset,
                multiplier*(k // line_length) + offset
            ]
            
        def calculate_position(ind):
            new_pos = [x for x in G.nodes[prev_nodes_E[0]]['pos']]
            for j in range(2):
                new_pos = [new_pos[i] + edge_vectors[j][i]*ind[j] for i in range(2)]
            return new_pos  
        
        def general_add_new_nodes(label, count, line_length, offset, debug=False):
            new_nodes = []
            for k in range(count):
                indecies = calculate_indecies(k, line_length, offset)
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
                offset=1./4, 
                debug=debug
            )
        
        def connect_I_nodes(I_nodes):
            # Add edge between middle nodes and previous middle node
            [G.add_edge(s, prev_node_I) for s in I_nodes]
    
        def add_new_E_nodes(debug=False):
            return general_add_new_nodes(
                label='E',
                count=9,
                line_length=3,
                offset=0,
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
        assign_variables(debug=True)
        update_prev_node_I()
        
        new_I_nodes = add_new_I_nodes(debug=True)
        connect_I_nodes(new_I_nodes)
        
        new_E_nodes = add_new_E_nodes(debug=True)
        connect_E_nodes(new_E_nodes, new_I_nodes)

        return True
