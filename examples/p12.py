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

    G.remove_edge(3, 4)
    upper = G.nodes[3]['pos']
    lower = G.nodes[4]['pos']
    G.add_node(7, label="E", pos=(upper[0] - (upper[0] - lower[0]) / 2, upper[1]), layer=1)
    G.add_edges_from([(3, 7), (4, 7)])

    draw_graph(G)
    P12_prim.apply(G)

    draw_graph(G)


