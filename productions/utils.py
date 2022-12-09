from typing import Dict, List
from networkx import Graph
from networkx.algorithms.isomorphism import GraphMatcher


def find_isomorphisms(G_main: Graph, G_to_find: Graph) -> List[Dict]:
    GM = GraphMatcher(G_main, G_to_find, node_match=lambda n1,
                      n2: n1['label'] == n2['label'])

    filtered_isomorphisms = []
    for isomorphism in GM.subgraph_isomorphisms_iter():
        if all([isomorphism.keys() != filtered_isomorphism.keys() for filtered_isomorphism in filtered_isomorphisms]):
            filtered_isomorphisms.append(isomorphism)

    return filtered_isomorphisms
