import networkx as nx
from productions.decorators import first_isomorphism
from typing import Dict, Optional

import math

def polar_coords_angle(center):
    def angle(pos):
        x, y = pos

        x = x - center[0]
        y = y - center[1]

        angle = math.atan2(y, x)

        return math.fmod(angle + math.pi, 2 * math.pi)

    return angle


class P12():
    left = nx.Graph()
    left.add_node(1, label='E')
    left.add_node(2, label='E')
    left.add_node(3, label='E')
    left.add_node(4, label='E')
    left.add_node(5, label='I')
    # connect center 'I' with all 'E'
    left.add_edges_from([(5, i) for i in range(1, 5)])
    # connect all 'E' in a square
    left.add_edges_from([(i, (i % 4) + 1) for i in range(1, 5)])

    @staticmethod
    @first_isomorphism(left)
    def apply(G: nx.Graph, isomorphism: Optional[Dict] = None):
        if isomorphism is None:
            return False


        nodes_in_G = list(isomorphism.keys())
        size = G.number_of_nodes()

        assert len(isomorphism) == 5, "Expected the isomorphism to have 5 nodes"

        I_node = None
        I_node_id = None
        E_pos = []
        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'I':
                I_node = G.nodes[node]
                I_node_id = node
            elif G.nodes[node]['label'] == 'E':
                E_pos.append(G.nodes[node]['pos'])

        layer = I_node['layer'] + 1
        current_node_id = size + 1


        E_pos = sorted(E_pos, key=polar_coords_angle(I_node['pos']), reverse=True)
        E_ids = []

        for pos in E_pos:
            G.add_node(current_node_id, pos=pos, label='E', layer=layer)
            E_ids.append(current_node_id)
            current_node_id += 1

        I_node['label'] = 'i'
        G.add_node(current_node_id, pos=I_node['pos'], label='I', layer=layer)
        new_I_node = (current_node_id, I_node['pos'])
        G.add_edge(I_node_id, new_I_node[0])

        for id in E_ids:
            G.add_edge(new_I_node[0], id)

        for i in range(len(E_ids) - 1):
            G.add_edge(E_ids[i], E_ids[i + 1])
        G.add_edge(E_ids[0], E_ids[-1])

        return True

class P12_prim():
    left = nx.Graph()
    left.add_node(1, label='E')
    left.add_node(2, label='E')
    left.add_node(3, label='E')
    left.add_node(4, label='E')
    left.add_node(5, label='I')
    left.add_node(6, label='E')
    # connect center 'I' with all 'E'
    left.add_edges_from([(5, i) for i in range(1, 5)])
    # connect all 'E' in a square
    left.add_edges_from([(i, (i % 4) + 1) for i in range(1, 5)])
    left.remove_edge(2, 3)
    left.add_edges_from([(2, 6), (3, 6)])

    @staticmethod
    @first_isomorphism(left)
    def apply(G: nx.Graph, isomorphism: Optional[Dict] = None):
        if isomorphism is None:
            return False


        nodes_in_G = list(isomorphism.keys())
        size = G.number_of_nodes()

        assert len(isomorphism) == 6, "Expected the isomorphism to have 6 nodes"

        I_node = None
        I_node_id = None
        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'I':
                I_node = G.nodes[node]
                I_node_id = node

        E_pos = []
        disconnected_node_pos = None
        for node in nodes_in_G:
            if G.nodes[node]['label'] == 'E':
                E_pos.append(G.nodes[node]['pos'])
                if not G.has_edge(I_node_id, node):
                    disconnected_node_pos = G.nodes[node]['pos']

        E_pos = sorted(E_pos, key=polar_coords_angle(I_node['pos']), reverse=True)

        layer = I_node['layer'] + 1
        current_node_id = size + 1

        E_ids = []
        disconnected_node_id = None
        for pos in E_pos:
            G.add_node(current_node_id, pos=pos, label='E', layer=layer)
            E_ids.append(current_node_id)

            if pos == disconnected_node_pos:
                disconnected_node_id = current_node_id
            current_node_id += 1

        I_node['label'] = 'i'
        G.add_node(current_node_id, pos=I_node['pos'], label='I', layer=layer)
        new_I_node_id = current_node_id
        G.add_edge(I_node_id, new_I_node_id)

        for id in E_ids:
            if id == disconnected_node_id:
                continue

            G.add_edge(new_I_node_id, id)

        for i in range(len(E_ids) - 1):
            G.add_edge(E_ids[i], E_ids[i + 1])
        G.add_edge(E_ids[0], E_ids[-1])

        return True

