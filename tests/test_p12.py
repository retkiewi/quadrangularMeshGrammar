
import matplotlib.pyplot as plt
import networkx as nx
import pytest

from productions import P12
from visualization import draw_graph

def test_p12_with_match():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(1, 1), layer=1)
    G.add_node(2, label='E', pos=(0, 0), layer=1)
    G.add_node(3, label='E', pos=(2, 0), layer=1)
    G.add_node(4, label='E', pos=(2, 2), layer=1)
    G.add_node(5, label='E', pos=(0, 2), layer=1)
    G.add_edges_from([(1, i) for i in range(2, 6)])

    P12.connect_square_edges(G, 2)

    assert True == P12.apply(G)

    assert [
        # first graph
        (1, {'label': 'I', 'pos': (1, 1), 'layer': 1}),
        (2, {'label': 'E', 'pos': (0, 0), 'layer': 1}),
        (3, {'label': 'E', 'pos': (2, 0), 'layer': 1}),
        (4, {'label': 'E', 'pos': (2, 2), 'layer': 1}),
        (5, {'label': 'E', 'pos': (0, 2), 'layer': 1}),
        # second graph
        (6, {'label': 'I', 'pos': (1, 1), 'layer': 2}),
        (7, {'label': 'E', 'pos': (0, 0), 'layer': 2}),
        (8, {'label': 'E', 'pos': (2, 0), 'layer': 2}),
        (9, {'label': 'E', 'pos': (2, 2), 'layer': 2}),
        (10, {'label': 'E', 'pos': (0, 2), 'layer': 2}),
    ] == list(G.nodes(data=True))

    assert {
        # first graph,
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 3), (2, 5), (3, 4), (4, 5),
        # connecting I nodes 
        (1, 6),
        # second graph
        (6, 7), (6, 8), (6, 9), (6, 10),
        (7, 8), (7, 10), (8, 9), (9, 10),
    } == set(G.edges)

def test_p12_without_match():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(1, 1), layer=1)
    G.add_node(2, label='E', pos=(0, 0), layer=1)
    G.add_node(3, label='E', pos=(2, 0), layer=1)
    G.add_node(4, label='E', pos=(2, 2), layer=1)
    G.add_node(5, label='E', pos=(0, 2), layer=1)
    G.add_edges_from([(1, i) for i in range(2, 6)])
    P12.connect_square_edges(G, 2)

    # remove a single edge from I node
    G.remove_edge(1, 2)

    assert False == P12.apply(G)


