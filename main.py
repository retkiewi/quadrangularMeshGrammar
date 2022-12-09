import sys
import argparse
import networkx as nx
from productions.p1 import P1
from productions.p2 import P2
import matplotlib.pyplot as plt
from visualization import draw_graph


def main(args):
    G = nx.Graph()
    G.add_node(1, label='El', pos=(0, 0), layer=0)

    P1.apply(G)
    P2.apply(G)

    draw_graph(G)
    # draw_graph(G, 0)
    # draw_graph(G, 2)
    plt.show()

if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    # add your args here
    main(parser.parse_args(sys.argv[1:]))
