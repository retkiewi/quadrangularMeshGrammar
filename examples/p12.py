import networkx as nx
from productions import P1, P12
from visualization import draw_graph

def show():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(0, 0), layer=0)

    P1.apply(G)
    P12.apply(G)
    P12.apply(G)

    draw_graph(G)


