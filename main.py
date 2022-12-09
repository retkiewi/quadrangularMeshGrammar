import sys
import argparse
import networkx as nx
from productions.p1 import P1
import matplotlib.pyplot as plt


def main(args):
    G = nx.Graph()
    G.add_node(1, node_color='red', label='El', pos=(0, 0))

    P1.apply(G)

    nx.draw(G, nx.get_node_attributes(G, 'pos'),
            labels=nx.get_node_attributes(G, 'label'), font_size=10)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # add your args here
    main(parser.parse_args(sys.argv[1:]))
