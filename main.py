import argparse
import sys
import matplotlib.pyplot as plt
import networkx as nx
from productions import P1, P2, P3, P4
from visualization import draw_graph


def main(args):
    variant = 2
    G = nx.Graph()
    if(variant == 0):
        # edge nodes 
        G.add_node(1, label='E', pos=(1, 0.5), layer=0)
        G.add_node(2, label='E', pos=(-0.5, 1), layer=0)
        G.add_node(3, label='E', pos=(-1, -0.5), layer=0)
        G.add_node(4, label='E', pos=(0.5, -1), layer=0)
        G.add_node(5, label='E', pos=(0.75, -0.25), layer=0)
        
        # middle node
        G.add_node(6, label='I', pos=(0, 0), layer=0)
        
        # connect middle to the edges
        [G.add_edge(6, i) for i in range(1, 5)]
        
        # create loop around the edges
        [G.add_edge(i, (i%5)+1) for i in range(1, 6)]
        
        print(P4.apply(G))
    elif (variant == 1):   
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
        
        print(P3.apply(G))
    elif (variant == 2):
        # edge nodes 
        G.add_node(1, label='E', pos=(0.5, -1), layer=0)
        G.add_node(2, label='E', pos=(1, 0.5), layer=0)
        G.add_node(3, label='E', pos=(-0.5, 1), layer=0)
        G.add_node(4, label='E', pos=(-1, -0.5), layer=0)
        G.add_node(5, label='E', pos=(-.25, -.75), layer=0)
        
        # middle node
        G.add_node(6, label='I', pos=(0, 0), layer=0)
        
        # connect middle to the edges
        [G.add_edge(6, i) for i in range(1, 5)]
        
        # create loop around the edges
        [G.add_edge(i, (i%5)+1) for i in range(1, 6)]
        
        print(P4.apply(G))  
    
    draw_graph(G,0)
    draw_graph(G,1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args(sys.argv[1:]))
