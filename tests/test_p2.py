import matplotlib.pyplot as plt
import networkx as nx
import pytest

from productions import P2

@pytest.fixture
def G():
    G = nx.Graph()
    G.add_node(1, label='el', pos=(1/2, 1/2), layer=0)
    G.add_node(2, label='I', pos=(1/2, 1/2), layer=1)
    G.add_node(3, label='E', pos=(0, 0), layer=1)
    G.add_node(4, label='E', pos=(1, 0), layer=1)
    G.add_node(5, label='E', pos=(1, 1), layer=1)
    G.add_node(6, label='E', pos=(0, 1), layer=1)
    G.add_edges_from([(2, i) for i in (1, 3, 4, 5, 6)])
    G.add_edges_from([(i, i+1) for i in range(3, 6)])
    G.add_edge(3, 6)

    return G

def test_p2_should_be_applied_full_proper_graph(G):
    assert True == P2.apply(G)

    assert [
     (1, {'label': 'el', 'pos': (0.5, 0.5), 'layer': 0}),
     (2, {'label': 'i', 'pos': (0.5, 0.5), 'layer': 1}),
     (3, {'label': 'E', 'pos': (0, 0), 'layer': 1}),
     (4, {'label': 'E', 'pos': (1, 0), 'layer': 1}),
     (5, {'label': 'E', 'pos': (1, 1), 'layer': 1}),
     (6, {'label': 'E', 'pos': (0, 1), 'layer': 1}), 
     (7, {'label': 'I', 'pos': (0.25, 0.5), 'layer': 2}), 
     (8, {'label': 'I', 'pos': (0.75, 0.5), 'layer': 2}), 
     (9, {'label': 'E', 'pos': (0, 0), 'layer': 2}), 
     (10, {'label': 'E', 'pos': (0.5, 0.0), 'layer': 2}), 
     (11, {'label': 'E', 'pos': (1, 0), 'layer': 2}), 
     (12, {'label': 'E', 'pos': (0, 1), 'layer': 2}), 
     (13, {'label': 'E', 'pos': (0.5, 1.0), 'layer': 2}), 
     (14, {'label': 'E', 'pos': (1, 1), 'layer': 2})] == list(G.nodes(data=True))

    assert {
    (3, 4), (12, 13), (2, 5), (11, 14), (2, 8), (13, 14), (7, 10), (7, 13), (4, 5), 
    (5, 6), (3, 6), (8, 11), (9, 10), (2, 4), (1, 2), (8, 14), (10, 11), (2, 7), 
    (7, 9), (7, 12), (9, 12), (8, 10), (10, 13), (2, 3), (8, 13), (2, 6)} == set(G.edges)


def test_p2_should_be_applied_without_edge_to_initial_node(G):
    G.remove_edge(1, 2)

    assert True == P2.apply(G)


def test_p2_should_be_applied_with_wrong_label_in_initial_node(G):
    G.nodes[1]['label'] = 'WRONG LABEL'

    assert True == P2.apply(G)

def test_p2_should_not_be_applied_because_of_missing_outer_edge(G):
    G.remove_edge(5, 6)

    assert False == P2.apply(G)

def test_p2_should_not_be_applied_because_of_missing_inner_edge(G):
    G.remove_edge(2, 6)

    assert False == P2.apply(G)

def test_p2_should_not_be_applied_because_of_wrong_outer_label(G):
    G.nodes[6]['label'] = 'WRONG LABEL'

    assert False == P2.apply(G)

def test_p2_should_not_be_applied_because_of_wrong_inner_label(G):
    G.nodes[2]['label'] = 'WRONG LABEL'

    assert False == P2.apply(G)


def test_p2_should_not_be_applied_because_of_surplus_node(G):
    G.remove_edge(4, 5)
    G.add_node(7, label='E', pos=(2, 1), layer=1)
    G.add_edge(4, 7)
    G.add_edge(5, 7)

    assert False == P2.apply(G)

def test_p2_should_not_be_applied_because_of_empty_graph():
    G = nx.Graph()

    assert False == P2.apply(G)

def test_p2_should_not_be_applied_because_of_initial_node_only():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)

    assert False == P2.apply(G)
