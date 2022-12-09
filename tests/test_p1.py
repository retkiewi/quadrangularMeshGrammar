import pytest
import networkx as nx

import matplotlib.pyplot as plt

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# from visualization import draw_graph
from productions import P1


def test_p1():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(0, 0), layer=0)

    assert True == P1.apply(G)

    # draw_graph(G)

    assert [(1, {'label': 'el', 'pos': (0, 0), 'layer': 0}),
            (2, {'label': 'I', 'pos': (0, -1), 'layer': 1}),
            (3, {'label': 'E', 'pos': (-0.5, -1.5), 'layer': 1}),
            (4, {'label': 'E', 'pos': (0.5, -1.5), 'layer': 1}),
            (5, {'label': 'E', 'pos': (0.5, -0.5), 'layer': 1}),
            (6, {'label': 'E', 'pos': (-0.5, -0.5), 'layer': 1})] == list(G.nodes(data=True))
    
    assert [(1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 6), (4, 5), (5, 6)] == list(G.edges)
