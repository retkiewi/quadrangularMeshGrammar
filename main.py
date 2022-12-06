import sys
import argparse
import networkx as nx
from productions.p1 import P1

def main(args):
    G = nx.Graph()
    G.add_node(1, label='El')
    P1.apply(G)

    nx.draw(G)


if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    # add your args here
    main(parser.parse_args(sys.argv[1:]))