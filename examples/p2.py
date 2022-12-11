import networkx as nx
from productions import P1, P2
from visualization import draw_graph

def show():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)

    P1.apply(G)
    P2.apply(G)
    P2.apply(G)
    P2.apply(G)

    P2.apply(G)
    P2.apply(G)
    P2.apply(G)
    P2.apply(G)
    P2.apply(G)
    P2.apply(G)

    draw_graph(G)
