import argparse
import sys
import matplotlib.pyplot as plt
import networkx as nx
from productions import P1, P2, P3, P4
from visualization import draw_graph


def main(args):
    first = False
    if(first):
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

        # P1.apply(G)
        print(P4.apply(G))

        draw_graph(G,1)
    else:    
        G = nx.Graph()
        G.add_node(1, label='I', pos=(0, 0), layer=0)
        G.add_node(2, label='E', pos=(1, 0.5), layer=0)
        G.add_node(3, label='E', pos=(-0.5, 1), layer=0)
        G.add_node(4, label='E', pos=(-1, -0.5), layer=0)
        G.add_node(5, label='E', pos=(0.5, -1), layer=0)
        [G.add_edge(1, i) for i in range(2, 6)]
        [G.add_edge(i, i+1) for i in range(2, 5)]
        G.add_edge(5, 2)
        P3.apply(G)
        draw_graph(G,1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))
