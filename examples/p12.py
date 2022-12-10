import matplotlib.pyplot as plt
import networkx as nx
from productions import P1, P12
from visualization import draw_graph

def offset_nodes_from(G, idx, offset):
    for node in list(G.nodes.keys()):
        if node >= idx:
            x, y = G.nodes[node]['pos']
            G.nodes[node]['pos'] = (x + offset[0], y + offset[1])


def show():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(0, 0), layer=0)

    P1.apply(G)
    size_after_p1 = G.number_of_nodes()

    P12.apply(G)
    offset_nodes_from(G, size_after_p1 + 1, (-1.25, -1.75))
    size_after_p12 = G.number_of_nodes()

    P12.apply(G)
    offset_nodes_from(G, size_after_p12 + 1, (1.25, 2 * -1.75))

    draw_graph(G)


