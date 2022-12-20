import networkx as nx
from productions.decorators import first_isomorphism_for_p13
from typing import Dict

class P13:
    left = nx.Graph()
    left.add_node(1, label='E')
    left.add_node(2, label='i')
    left.add_node(3, label='i')
    left.add_node(4, label='I')
    left.add_node(5, label='I')
    left.add_node(6, label='I')
    left.add_node(7, label='E')
    left.add_node(8, label='E')
    left.add_node(9, label='E')
    left.add_node(10, label='E')
    left.add_node(11, label='E')
    left.add_edge(1, 2)
    left.add_edge(1, 3)
    left.add_edge(2, 4)
    left.add_edge(2, 5)
    left.add_edge(3, 6)
    left.add_edge(4, 7)
    left.add_edge(4, 8)
    left.add_edge(5, 8)
    left.add_edge(5, 9)
    left.add_edge(6, 10)
    left.add_edge(6, 11)
    left.add_edge(7, 8)
    left.add_edge(8, 9)
    left.add_edge(10, 11)

    @staticmethod
    @first_isomorphism_for_p13(left)
    def apply(G: nx.Graph, isomorphism: Dict = None):
        if isomorphism is None:
            return False

        nodes_in_G = list(isomorphism.keys())
        E_nodes = []
        E_coeff = set()

        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'E':
                adjacency = G.adj[node]
                is_connected_to_i = False
                for neighbour in adjacency:
                    if G.nodes[neighbour]['label'] == 'i':
                        is_connected_to_i = True
                        break
                if not is_connected_to_i:
                    E_nodes.append(node)
                    E_coeff.add(G.nodes[node]['pos'])

        E_coeff = sorted(list(E_coeff))

        to_remove_1 = None
        to_remove_2 = None
        I_to_connect = None

        for node in E_nodes:
            adjacency = G.adj[node]
            pos = G.nodes[node]['pos']
            if pos == E_coeff[0] or pos == E_coeff[2]:
                to_remove = True
                for neighbour in adjacency:
                    if G.nodes[neighbour]['label'] == 'E' and G.nodes[neighbour]['pos'] == E_coeff[1]:
                        to_remove = False
                if to_remove:
                    to_remove_1 = node
                    for neighbour in adjacency:
                        if G.nodes[neighbour]['label'] == 'E' and neighbour in nodes_in_G:
                            to_remove_2 = neighbour
                        if G.nodes[neighbour]['label'] == 'I' and neighbour in nodes_in_G:
                            I_to_connect = neighbour
                    break

        E_nodes.remove(to_remove_1)
        E_nodes.remove(to_remove_2)
        G.remove_node(to_remove_1)
        G.remove_node(to_remove_2)

        for node in E_nodes:
            if G.nodes[node]['pos'] != E_coeff[1]:
                G.add_edge(node, I_to_connect)

        return True
