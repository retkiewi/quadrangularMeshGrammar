import networkx as nx
from visualization import draw_graph

from productions import P13


def get_basic_graph():
    basic_graph = nx.Graph()
    basic_graph.add_node(1, label='E', pos=(0, 6), layer=0)
    basic_graph.add_node(2, label='i', pos=(-1, 5), layer=0)
    basic_graph.add_node(3, label='i', pos=(1, 5), layer=0)
    basic_graph.add_node(4, label='I', pos=(-2, 3), layer=0)
    basic_graph.add_node(5, label='I', pos=(-2, 1), layer=0)
    basic_graph.add_node(6, label='I', pos=(2, 2), layer=0)
    basic_graph.add_node(7, label='E', pos=(0, 4), layer=0)
    basic_graph.add_node(8, label='E', pos=(0, 2), layer=0)
    basic_graph.add_node(9, label='E', pos=(0, 0), layer=0)
    basic_graph.add_node(10, label='E', pos=(0, 4), layer=0)
    basic_graph.add_node(11, label='E', pos=(0, 0), layer=0)
    basic_graph.add_edge(1, 2)
    basic_graph.add_edge(1, 3)
    basic_graph.add_edge(2, 4)
    basic_graph.add_edge(2, 5)
    basic_graph.add_edge(3, 6)
    basic_graph.add_edge(4, 7)
    basic_graph.add_edge(4, 8)
    basic_graph.add_edge(5, 8)
    basic_graph.add_edge(5, 9)
    basic_graph.add_edge(6, 10)
    basic_graph.add_edge(6, 11)
    basic_graph.add_edge(7, 8)
    basic_graph.add_edge(8, 9)
    basic_graph.add_edge(10, 11)
    return basic_graph


def test_p13_should_apply_basic():
    G = get_basic_graph()

    assert P13.apply(G) is True

    assert [(1, {'label': 'E', 'pos': (0, 6), 'layer': 0}),
            (2, {'label': 'i', 'pos': (-1, 5), 'layer': 0}),
            (3, {'label': 'i', 'pos': (1, 5), 'layer': 0}),
            (4, {'label': 'I', 'pos': (-2, 3), 'layer': 0}),
            (5, {'label': 'I', 'pos': (-2, 1), 'layer': 0}),
            (6, {'label': 'I', 'pos': (2, 2), 'layer': 0}),
            (7, {'label': 'E', 'pos': (0, 4), 'layer': 0}),
            (8, {'label': 'E', 'pos': (0, 2), 'layer': 0}),
            (9, {'label': 'E', 'pos': (0, 0), 'layer': 0})] == list(G.nodes(data=True))

    assert {(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (4, 8), (5, 8), (5, 9), (6, 7), (6, 9), (7, 8), (8, 9)} \
           == set(G.edges)


def test_p13_should_apply_with_added_nodes():
    G = get_basic_graph()
    G.add_node(12, label='E', pos=(0, 7), layer=0)
    G.add_edge(12, 1)
    G.add_edge(12, 2)
    G.add_edge(12, 3)
    G.add_edge(12, 4)
    G.add_edge(12, 5)

    assert P13.apply(G) is True

    assert [(1, {'label': 'E', 'pos': (0, 6), 'layer': 0}),
            (2, {'label': 'i', 'pos': (-1, 5), 'layer': 0}),
            (3, {'label': 'i', 'pos': (1, 5), 'layer': 0}),
            (4, {'label': 'I', 'pos': (-2, 3), 'layer': 0}),
            (5, {'label': 'I', 'pos': (-2, 1), 'layer': 0}),
            (6, {'label': 'I', 'pos': (2, 2), 'layer': 0}),
            (7, {'label': 'E', 'pos': (0, 4), 'layer': 0}),
            (8, {'label': 'E', 'pos': (0, 2), 'layer': 0}),
            (9, {'label': 'E', 'pos': (0, 0), 'layer': 0}),
            (12, {'label': 'E', 'pos': (0, 7), 'layer': 0})] == list(G.nodes(data=True))

    assert {(1, 2), (1, 3), (1, 12), (2, 4), (2, 5), (2, 12), (3, 6), (3, 12), (4, 7), (4, 8), (4, 12), (5, 8), (5, 9),
            (5, 12), (6, 7), (6, 9), (7, 8), (8, 9)} == set(G.edges)


def test_p13_should_not_apply_with_added_nodes():
    G = get_basic_graph()
    G.add_node(12, label='E', pos=(0, 7), layer=0)
    G.remove_edge(1, 2)
    G.add_edge(1, 12)
    G.add_edge(12, 2)

    assert P13.apply(G) is False


def test_p13_should_not_apply_node_removed():
    for i in range(1, 12):
        G = get_basic_graph()

        G.remove_node(i)

        assert P13.apply(G) is False


def test_p13_should_not_apply_edge_removed():
    for i in range(0, 14):
        G = get_basic_graph()

        (v1, v2) = list(G.edges)[i]
        G.remove_edge(v1, v2)

        assert P13.apply(G) is False


def test_p13_should_not_apply_node_label_changed():
    for i in range(1, 12):
        G = get_basic_graph()

        G.nodes[i]['label'] = 'm'

        assert P13.apply(G) is False


def test_p13_should_not_apply_wrong_coordinates_1():
    G = nx.Graph()
    G.add_node(1, label='E', pos=(0, 6), layer=0)
    G.add_node(2, label='i', pos=(-1, 5), layer=0)
    G.add_node(3, label='i', pos=(1, 5), layer=0)
    G.add_node(4, label='I', pos=(-2, 3), layer=0)
    G.add_node(5, label='I', pos=(-2, 1), layer=0)
    G.add_node(6, label='I', pos=(2, 2), layer=0)
    G.add_node(7, label='E', pos=(0, 4), layer=0)
    G.add_node(8, label='E', pos=(0, 2), layer=0)
    G.add_node(9, label='E', pos=(0, 0), layer=0)
    G.add_node(10, label='E', pos=(0, 5), layer=0)
    G.add_node(11, label='E', pos=(0, 0), layer=0)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 6)
    G.add_edge(4, 7)
    G.add_edge(4, 8)
    G.add_edge(5, 8)
    G.add_edge(5, 9)
    G.add_edge(6, 10)
    G.add_edge(6, 11)
    G.add_edge(7, 8)
    G.add_edge(8, 9)
    G.add_edge(10, 11)

    assert P13.apply(G) is False


def test_p13_should_not_apply_wrong_coordinates_2():
    G = nx.Graph()
    G.add_node(1, label='E', pos=(0, 6), layer=0)
    G.add_node(2, label='i', pos=(-1, 5), layer=0)
    G.add_node(3, label='i', pos=(1, 5), layer=0)
    G.add_node(4, label='I', pos=(-2, 3), layer=0)
    G.add_node(5, label='I', pos=(-2, 1), layer=0)
    G.add_node(6, label='I', pos=(2, 2), layer=0)
    G.add_node(7, label='E', pos=(0, 4), layer=0)
    G.add_node(8, label='E', pos=(5, 10), layer=0)
    G.add_node(9, label='E', pos=(0, 0), layer=0)
    G.add_node(10, label='E', pos=(0, 4), layer=0)
    G.add_node(11, label='E', pos=(0, 0), layer=0)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 6)
    G.add_edge(4, 7)
    G.add_edge(4, 8)
    G.add_edge(5, 8)
    G.add_edge(5, 9)
    G.add_edge(6, 10)
    G.add_edge(6, 11)
    G.add_edge(7, 8)
    G.add_edge(8, 9)
    G.add_edge(10, 11)

    assert P13.apply(G) is False


def test_p13_should_not_apply_wrong_coordinates_3():
    G = nx.Graph()
    G.add_node(1, label='E', pos=(0, 6), layer=0)
    G.add_node(2, label='i', pos=(-1, 5), layer=0)
    G.add_node(3, label='i', pos=(1, 5), layer=0)
    G.add_node(4, label='I', pos=(-2, 3), layer=0)
    G.add_node(5, label='I', pos=(-2, 1), layer=0)
    G.add_node(6, label='I', pos=(2, 2), layer=0)
    G.add_node(7, label='E', pos=(0, 2), layer=0)
    G.add_node(8, label='E', pos=(0, 0), layer=0)
    G.add_node(9, label='E', pos=(0, 4), layer=0)
    G.add_node(10, label='E', pos=(0, 4), layer=0)
    G.add_node(11, label='E', pos=(0, 0), layer=0)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 6)
    G.add_edge(4, 7)
    G.add_edge(4, 8)
    G.add_edge(5, 8)
    G.add_edge(5, 9)
    G.add_edge(6, 10)
    G.add_edge(6, 11)
    G.add_edge(7, 8)
    G.add_edge(8, 9)
    G.add_edge(10, 11)

    assert P13.apply(G) is False
