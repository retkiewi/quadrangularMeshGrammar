import networkx as nx
from productions.decorators import first_isomorphism
from typing import Dict


class P1():
    left = nx.Graph()
    left.add_node(1, label='El')

    @staticmethod
    @first_isomorphism(left)
    def apply(G: nx.Graph, isomorphism: Dict = None):
        if isomorphism is None:
            return False

        El_node_id = list(isomorphism.keys())[0]
        El_node = (El_node_id, G.nodes[El_node_id])

        El_node[1]['label'] = 'el'
        layer = El_node[1]['layer']
        size = G.number_of_nodes()

        G.add_node(size + 1, label='I', pos=(1/2, 1/2), layer=layer+1)
        G.add_edge(size, size+1)

        G.add_node(size + 2, label='E', pos=(0,0), layer=layer+1)
        G.add_node(size + 3, label='E', pos=(1,0), layer=layer+1)
        G.add_node(size + 4, label='E', pos=(0,1), layer=layer+1)
        G.add_node(size + 5, label='E', pos=(1,1), layer=layer+1)

        G.add_edges_from([(size + 1, size + i) for i in (2, 3, 4, 5)])
        G.add_edge(size + 2, size + 3)
        G.add_edge(size + 2, size + 4)
        G.add_edge(size + 3, size + 5)
        G.add_edge(size + 4, size + 5)

        return True
