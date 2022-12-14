import matplotlib.pyplot as plt
import networkx as nx
import pytest

from productions import P3


def test_p3_flat():
    G = nx.Graph()
    # edge nodes 
    G.add_node(1, label='E', pos=(1, 0), layer=0)
    G.add_node(2, label='E', pos=(0, 1), layer=0)
    G.add_node(3, label='E', pos=(-1, 0), layer=0)
    G.add_node(4, label='E', pos=(0, -1), layer=0)
    
    # middle node
    G.add_node(5, label='I', pos=(0, 0), layer=0)
    
    # connect middle to the edges
    [G.add_edge(5, i) for i in range(1, 5)]
    
    # create loop around the edges
    [G.add_edge(i, (i%4)+1) for i in range(1, 5)]
    
    assert True == P3.apply(G)

    assert G.nodes[5]['label'] == 'i'


def test_p3_rotated():
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
    
    assert True == P3.apply(G)

    assert G.nodes[5]['label'] == 'i'

def test_p4_wrong_label():
    G = nx.Graph()
    # edge nodes 
    G.add_node(1, label='E', pos=(1, 0.5), layer=0)
    G.add_node(2, label='E', pos=(-0.5, 1), layer=0)
    G.add_node(3, label='E', pos=(-1, -0.5), layer=0)
    G.add_node(4, label='E', pos=(0.5, -1), layer=0)
    
    # middle node
    G.add_node(5, label='E', pos=(0, 0), layer=0)
    
    # connect middle to the edges
    [G.add_edge(5, i) for i in range(1, 5)]
    
    # create loop around the edges
    [G.add_edge(i, (i%4)+1) for i in range(1, 5)]
    
    assert False == P3.apply(G)

def test_p4_wrong_graph():
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
    
    assert False == P3.apply(G)