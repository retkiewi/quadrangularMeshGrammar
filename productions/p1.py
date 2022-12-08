import networkx as nx

class P1():
    left = nx.Graph()
    left.add_node(1, label='El')

    @staticmethod
    def apply(G: nx.Graph, offset = 1):
        El_node = None
        for node in G.nodes(data=True):
            if node[1]['label'] == 'El':
                El_node = node
                break

        if not El_node: return False

        El_node[1]['label'] = 'el'
        (pos_x, pos_y) = El_node[1]['pos']
        G.add_node(El_node[0]+1, label='I', pos=(pos_x, pos_y-offset))
        G.add_edge(El_node[0], El_node[0]+1)

        I_node = (El_node[0]+1, G.nodes[El_node[0]+1])
        (pos_x, pos_y) = I_node[1]['pos']

        G.add_node(I_node[0]+1, label='E', pos=(pos_x-offset/2, pos_y-offset/2))
        G.add_edge(I_node[0], I_node[0]+1)
        
        G.add_node(I_node[0]+2, label='E', pos=(pos_x+offset/2, pos_y-offset/2))
        G.add_edge(I_node[0], I_node[0]+2)
        
        G.add_node(I_node[0]+3, label='E', pos=(pos_x+offset/2, pos_y+offset/2))
        G.add_edge(I_node[0], I_node[0]+3)
        
        G.add_node(I_node[0]+4, label='E', pos=(pos_x-offset/2, pos_y+offset/2))
        G.add_edge(I_node[0], I_node[0]+4)

        G.add_edge(I_node[0]+1, I_node[0]+2)
        G.add_edge(I_node[0]+2, I_node[0]+3)
        G.add_edge(I_node[0]+3, I_node[0]+4)
        G.add_edge(I_node[0]+4, I_node[0]+1)

        return True