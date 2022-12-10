import networkx as nx
from productions.decorators import first_isomorphism
from typing import Dict

class P12():

    @staticmethod
    def connect_square_edges(G: nx.Graph, start_idx: int):
        end_idx = start_idx + 3

        # add border edges
        edges = [(i, i + 1) for i in range(start_idx, end_idx)]
        edges.append((start_idx, end_idx))
        G.add_edges_from(edges)

    left = nx.Graph()
    left.add_node(1, label='I')
    left.add_node(2, label='E')
    left.add_node(3, label='E')
    left.add_node(4, label='E')
    left.add_node(5, label='E')
    left.add_edges_from([(1, i) for i in range(2, 6)])

    connect_square_edges.__func__(left, 2)

    @staticmethod
    @first_isomorphism(left)
    def apply(G: nx.Graph, isomorphism: Dict = None):
        if isomorphism is None:
            return False


        nodes_in_G = list(isomorphism.keys())
        size = G.number_of_nodes()

        assert len(isomorphism) == 5, "Expected the isomorphism to have 5 nodes"

        I_node = None
        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'I':
                I_node = G.nodes[node]

        layer = I_node['layer']

        node_mapping = {}

        # for each node from isomorphism create a new node
        # with the same label and position, also store the
        # nodes mapping for edge creation
        current_node_id = size + 1
        for node_id in nodes_in_G:
            node = G.nodes[node_id]
            G.add_node(current_node_id, pos=node['pos'], label=node['label'], layer=layer+1)
            node_mapping[node_id] = current_node_id

            if node['label'] == 'I':
                G.add_edge(node_id, current_node_id)

            current_node_id += 1


        added_edges = []
        for node in nodes_in_G:
            for (a, b) in G.edges(node):
                # if the edge links to a node from outside
                # the isomorphism then ignore it
                if a not in nodes_in_G or b not in nodes_in_G:
                    continue

                edge_from = node_mapping[a]
                edge_to = node_mapping[b]

                if (edge_from, edge_to) in added_edges:
                    continue

                added_edges.append((edge_from, edge_to))
                added_edges.append((edge_to, edge_from))
                G.add_edge(edge_from, edge_to)

        return True
