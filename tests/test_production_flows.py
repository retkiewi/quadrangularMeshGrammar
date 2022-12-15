import networkx as nx
from productions import P1, P2


def test_p1_p2_p2_p2_should_create_correct_structure():
    G = nx.Graph()
    G.add_node(1, label='El', pos=(1/2, 1/2), layer=0)

    assert True == P1.apply(G)
    assert True == P2.apply(G)
    assert True == P2.apply(G)
    assert True == P2.apply(G)

    expected_nodes = [
        {'label': 'el', 'pos': (0.5, 0.5), 'layer': 0},
        {'label': 'i', 'pos': (0.5, 0.5), 'layer': 1},
        {'label': 'E', 'pos': (0, 0), 'layer': 1},
        {'label': 'E', 'pos': (1, 0), 'layer': 1},
        {'label': 'E', 'pos': (0, 1), 'layer': 1},
        {'label': 'E', 'pos': (1, 1), 'layer': 1},
        # SECOND LAYER
        {'label': 'i', 'pos': (0.25, 0.5), 'layer': 2},
        {'label': 'i', 'pos': (0.75, 0.5), 'layer': 2},
        {'label': 'E', 'pos': (0, 0), 'layer': 2},
        {'label': 'E', 'pos': (0.5, 0), 'layer': 2},
        {'label': 'E', 'pos': (0, 1), 'layer': 2},
        {'label': 'E', 'pos': (0.5, 1), 'layer': 2},
        {'label': 'E', 'pos': (1, 0), 'layer': 2},
        {'label': 'E', 'pos': (1, 1), 'layer': 2},
        # THIRD LAYER
        {'label': 'I', 'pos': (0.125, 0.5), 'layer': 3},
        {'label': 'I', 'pos': (0.375, 0.5), 'layer': 3},
        {'label': 'E', 'pos': (0, 0), 'layer': 3},
        {'label': 'E', 'pos': (0.25, 0), 'layer': 3},
        {'label': 'E', 'pos': (0, 1), 'layer': 3},
        {'label': 'E', 'pos': (0.25, 1), 'layer': 3},
        {'label': 'E', 'pos': (0.5, 0), 'layer': 3},
        {'label': 'E', 'pos': (0.5, 1), 'layer': 3},

        {'label': 'I', 'pos': (0.625, 0.5), 'layer': 3},
        {'label': 'I', 'pos': (0.875, 0.5), 'layer': 3},
        {'label': 'E', 'pos': (0.5, 0), 'layer': 3},
        {'label': 'E', 'pos': (0.75, 0), 'layer': 3},
        {'label': 'E', 'pos': (0.5, 1), 'layer': 3},
        {'label': 'E', 'pos': (0.75, 1), 'layer': 3},
        {'label': 'E', 'pos': (1, 0), 'layer': 3},
        {'label': 'E', 'pos': (1, 1), 'layer': 3},
    ]

    assert len(G.nodes()) == len(expected_nodes)

    for _, data in G.nodes(data=True):
        assert data in expected_nodes
        expected_nodes.remove(data)

    assert {(1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4),
            (3, 5), (4, 6), (5, 6), (2, 7), (7, 9), (7, 10),
            (7, 12), (2, 8), (8, 10), (8, 11), (8, 13),
            (7, 13), (8, 14), (9, 10), (10, 11), (9, 12),
            (15, 21), (17, 20), (16, 19), (15, 17), (7, 16),
            (21, 22), (16, 22), (15, 20), (18, 19), (16, 21),
            (19, 22), (16, 18), (7, 15), (18, 21), (17, 18),
            (20, 21), (15, 18), (10, 13), (13, 14), (11, 14),
            (12, 13), (24, 30), (8, 24), (24, 27), (8, 23),
            (26, 27), (25, 28), (24, 26), (27, 30), (28, 29),
            (23, 26), (24, 29), (23, 29), (23, 28), (26, 29),
            (23, 25), (25, 26), (29, 30)} == set(G.edges)
