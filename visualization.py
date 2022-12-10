import networkx as nx
import matplotlib.pyplot as plt

def map_label_to_color(label):
    color_map = {'el' : '#ff0000', 'i': '#ffa500' , 'e':'#5e90d7'}
    return color_map.get(label.lower(), '#c1c1c1') # get whats under label or default value

def map_pos_to_vis_pos(pos, layer):
    x_size = 10
    y_size = 10
    y_offset = 6
    
    # version with increasing x size
    # if layer >= 3:
    #     x_size *= 2**(layer-2)

    return (x_size * pos[0], -(y_size * pos[1] + layer * (y_size+y_offset)))

def get_layer_subgraph(graph: nx.Graph, layer: int):
    layer_nodes = []
    for node in graph.nodes(data=True):
        if node[1]['layer'] == layer:
            layer_nodes.append(node[0])
    return graph.subgraph(layer_nodes)

def draw_graph(graph: nx.Graph, layer=None):
    if layer is not None:
        graph = get_layer_subgraph(graph, layer)

    labels = nx.get_node_attributes(graph,'label')
    node_colors = list(map(map_label_to_color, labels.values()))

    vis_pos = nx.get_node_attributes(graph,'pos')
    if layer is None:
        vis_pos = {node: map_pos_to_vis_pos(data['pos'], data['layer']) for node, data in graph.nodes(data=True)}

    nx.draw(graph, pos=vis_pos,
            labels=labels, font_size=12,
            node_size=300, node_color=node_colors)
    plt.show()
