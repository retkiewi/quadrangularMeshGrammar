from typing import Dict, List

from networkx import Graph
from networkx.algorithms.isomorphism import GraphMatcher


def find_isomorphisms(G_main: Graph, G_to_find: Graph) -> List[Dict]:
    GM = GraphMatcher(G_main, G_to_find, node_match=lambda n1, n2: n1['label'] == n2['label'])

    filtered_isomorphisms = []
    for isomorphism in GM.subgraph_isomorphisms_iter():
        if all([isomorphism.keys() != filtered_isomorphism.keys() for filtered_isomorphism in filtered_isomorphisms]):
            filtered_isomorphisms.append(isomorphism)

    return filtered_isomorphisms


def find_isomorphisms_for_p13(G_main: Graph, G_to_find: Graph) -> List[Dict]:
    isomorphisms = find_isomorphisms(G_main, G_to_find)

    filtered_isomorphisms_for_p13 = []

    for isomorphism in isomorphisms:
        is_correct = True
        E_coeff = set()
        E_nodes = []
        nodes_in_graph = list(isomorphism.keys())
        for node in nodes_in_graph:
            if G_main.nodes[node]['label'] == 'E':
                adjacency = G_main.adj[node]
                is_connected_to_i = False
                for neighbour in adjacency:
                    if G_main.nodes[neighbour]['label'] == 'i':
                        is_connected_to_i = True
                        break
                if not is_connected_to_i:
                    E_coeff.add(G_main.nodes[node]['pos'])
                    E_nodes.append(node)
        if len(E_coeff) != 3:
            is_correct = False
        E_coeff = sorted(list(E_coeff))
        if (E_coeff[0][0] + E_coeff[2][0]) / 2 != E_coeff[1][0] or (E_coeff[0][1] + E_coeff[2][1]) / 2 != E_coeff[1][1]:
            is_correct = False
        for node in E_nodes:
            if (G_main.nodes[node]['pos'] in [E_coeff[0], E_coeff[2]]) and len(list(G_main.adj[node])) != 2:
                is_correct = False
            if (G_main.nodes[node]['pos'] == E_coeff[1]) and len(list(G_main.adj[node])) != 4:
                is_correct = False
        if is_correct:
            filtered_isomorphisms_for_p13.append(isomorphism)

    return filtered_isomorphisms_for_p13
