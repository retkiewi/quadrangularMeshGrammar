import networkx as nx

class P1():
    left = nx.Graph()
    left.add_node(1, label='El')

    @staticmethod
    def apply(G: nx.Graph, offset = 1):
        El_node = None
        
        # find isos and get pick first one
        isomorphisms = find_isomorphisms(G, P1.left)
        if len(isomorphisms) < 1:
            return False
        iso = isomorphisms[0]
        nodes_in_G = list(iso.keys())
        if len(nodes_in_G) != 1:
            return False
        node_id = nodes_in_G[0]
        El_node = G.nodes(data=True)[node_id]

        if not El_node: return False

        El_node['label'] = 'el'
        (pos_x, pos_y) = El_node['pos']
        G.add_node(node_id+1, label='I', pos=(pos_x, pos_y-offset))
        G.add_edge(node_id, node_id+1)

        I_node = (node_id+1, G.nodes[node_id+1])
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
