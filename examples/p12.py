import networkx as nx
from productions import P1, P12
from productions.p12 import P12_prim
from visualization import draw_graph

def show():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(0, 0), layer=0)

    P1.apply(G)
    P12.apply(G)
    P12.apply(G)

    draw_graph(G)

def show_prim():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(0, 0), layer=0)

    P1.apply(G)

    G.remove_edge(4, 6)
    upper = G.nodes[4]['pos']
    lower = G.nodes[6]['pos']
    G.add_node(7, label="E", pos=(upper[0], upper[1] - (upper[1] - lower[1]) / 2), layer=1)
    G.add_edges_from([(4, 7), (6, 7)])

    P12_prim.apply(G)

    draw_graph(G)


