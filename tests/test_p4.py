import matplotlib.pyplot as plt
import networkx as nx
import pytest

from productions import P4
# from visualization import draw_graph


def test_p4_horizontal():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)    
    G.add_node(3, label='E', pos=(0, 1), layer=0)
    G.add_node(6, label='E', pos=(0.5, 0), layer=0)
    G.add_node(4, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    
    # connect middle to the edges
    G.add_edges_from([(1, i) for i in range(2, 6)])
    
    # edge nodes
    G.add_edge(2, 3)
    G.add_edge(3, 5)
    G.add_edge(5, 4)
    G.add_edge(4, 6)
    G.add_edge(6, 2)
    assert True == P4.apply(G)

    assert G.nodes[9]['pos'][0] == 1.0
    assert G.nodes[9]['pos'][1] == 0.0

    assert G.nodes[10]['pos'][0] == 0.5
    assert G.nodes[10]['pos'][1] == 0.0

    assert G.nodes[11]['pos'][0] == 0.0
    assert G.nodes[11]['pos'][1] == 0.0

    assert G.nodes[12]['pos'][0] == 1.0
    assert G.nodes[12]['pos'][1] == 1.0

    assert G.nodes[13]['pos'][0] == 0.5
    assert G.nodes[13]['pos'][1] == 1.0


def test_p4_vertical():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)    
    G.add_node(3, label='E', pos=(0, 1), layer=0)
    G.add_node(4, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    G.add_node(6, label='E', pos=(0, 0.5), layer=0)
    
    # connect middle to the edges
    G.add_edges_from([(1, i) for i in range(2, 6)])
    
    # edge nodes
    G.add_edge(2, 6)
    G.add_edge(6, 3)
    G.add_edge(3, 5)
    G.add_edge(5, 4)
    G.add_edge(4, 2)
    assert True == P4.apply(G)

def test_p4_wrong_hanging_node_position():
    G = nx.Graph()
    G.add_node(1, label='I', pos=(0.5, 0.5), layer=0)
    G.add_node(2, label='E', pos=(0, 0), layer=0)    
    G.add_node(3, label='E', pos=(0, 1), layer=0)
    G.add_node(4, label='E', pos=(1, 0), layer=0)
    G.add_node(5, label='E', pos=(1, 1), layer=0)
    G.add_node(6, label='E', pos=(0, 0.6), layer=0)
    
    # connect middle to the edges
    G.add_edges_from([(1, i) for i in range(2, 6)])
    
    # edge nodes
    G.add_edge(2, 6)
    G.add_edge(6, 3)
    G.add_edge(3, 5)
    G.add_edge(5, 4)
    G.add_edge(4, 2)
    assert False == P4.apply(G)

def test_p4_wrong_graph():
    G = nx.Graph()
    # edge nodes 
    G.add_node(1, label='E', pos=(1, 0.5), layer=0)
    G.add_node(2, label='E', pos=(-0.5, 1), layer=0)
    G.add_node(3, label='E', pos=(-1, -0.5), layer=0)
    G.add_node(4, label='E', pos=(0.5, -1), layer=0)
    
    # middle node
    G.add_node(5, label='I', pos=(0, 0), layer=0)
    
    # connect middle to the edges
    [G.add_edge(5, i) for i in range(1, 5)]
    
    # create loop around the edges
    [G.add_edge(i, (i%4)+1) for i in range(1, 5)]
    
    assert False == P4.apply(G)