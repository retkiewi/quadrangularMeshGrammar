import networkx as nx
from productions import P1


def test_p1_should_be_applied():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)

    assert True == P1.apply(G)

    assert [(1, {'label': 'el', 'pos': (0.5, 0.5), 'layer': 0}),
            (2, {'label': 'I', 'pos': (0.5, 0.5), 'layer': 1}),
            (3, {'label': 'E', 'pos': (0, 0), 'layer': 1}),
            (4, {'label': 'E', 'pos': (1, 0), 'layer': 1}),
            (5, {'label': 'E', 'pos': (0, 1), 'layer': 1}),
            (6, {'label': 'E', 'pos': (1, 1), 'layer': 1})] == list(G.nodes(data=True))

    assert {(1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4),
            (3, 5), (4, 6), (5, 6)} == set(G.edges)


def test_p1_cant_be_applied():
    G = nx.Graph()
    G.add_node(1, label='el', pos=(1/2, 1/2), layer=0)

    assert False == P1.apply(G)

    assert [(1, {'label': 'el', 'pos': (0.5, 0.5), 'layer': 0})
            ] == list(G.nodes(data=True))

    assert set() == set(G.edges)
