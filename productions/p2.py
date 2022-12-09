import networkx as nx
from productions.decorators import first_isomorphism
from typing import Dict


class P2():
    left = nx.Graph()
    left.add_node(1, label='I')
    left.add_node(2, label='E')
    left.add_node(3, label='E')
    left.add_node(4, label='E')
    left.add_node(5, label='E')
    left.add_edges_from([(1, i) for i in range(2,6)])
    left.add_edges_from([(2,3), (2,4)])
    left.add_edge(3, 5)
    left.add_edge(4, 5)

    @staticmethod
    @first_isomorphism(left)
    def apply(G: nx.Graph, offset = 1, isomorphism: Dict = None):
        if isomorphism is None:
            return False

        nodes_in_G = list(isomorphism.keys())
        
        I_node = None
        I_node_id = None
        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'I':
                I_node = G.nodes[node]
                I_node_id = node

        I_node['label'] = 'i'

        (pos_x, pos_y) = I_node['pos']
        layer = I_node['layer']

        size = G.number_of_nodes()

        G.add_node(size+1, label='I', pos=(pos_x-offset/2, pos_y-3/2*offset), layer=layer+1)
        G.add_node(size+2, label='I', pos=(pos_x+offset/2, pos_y-3/2*offset), layer=layer+1)
        G.add_edge(size+1, I_node_id)
        G.add_edge(size+2, I_node_id)

        G.add_node(size+3, label='E', pos=(pos_x-offset, pos_y-offset), layer=layer+1)
        G.add_node(size+4, label='E', pos=(pos_x, pos_y-offset), layer=layer+1)
        G.add_node(size+5, label='E', pos=(pos_x+offset, pos_y-offset), layer=layer+1)

        G.add_node(size+6, label='E', pos=(pos_x-offset, pos_y-2*offset), layer=layer+1)
        G.add_node(size+7, label='E', pos=(pos_x, pos_y-2*offset), layer=layer+1)
        G.add_node(size+8, label='E', pos=(pos_x+offset, pos_y-2*offset), layer=layer+1)

        G.add_edges_from([(size+1, size+i) for i in (3,4,6,7)])
        G.add_edges_from([(size+2, size+i) for i in (4,5,7,8)])
        G.add_edges_from([(size+i, size+i+1) for i in (3,4,6,7)])
        G.add_edge(size+3, size+6)
        G.add_edge(size+4, size+7)
        G.add_edge(size+5, size+8)

        return True
