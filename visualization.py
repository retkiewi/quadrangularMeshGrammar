import networkx as nx
import matplotlib.pyplot as plt

def map_label_to_color(label):
    color_map = {'el' : '#ff0000', 'i': '#ffa500' , 'e':'#5e90d7'}
    return color_map.get(label.lower(), '#c1c1c1') # get whats under label or default value

def draw_graph(graph, layer=None):
    if layer != None:
        layer_nodes = []
        for node in graph.nodes(data=True):
            if node[1]['layer'] == layer:
                layer_nodes.append(node[0])
        graph = graph.subgraph(layer_nodes)

    labels = nx.get_node_attributes(graph,'label')
    node_colors = list(map(map_label_to_color, labels.values()))

    nx.draw(graph, pos=nx.get_node_attributes(graph,'pos'),
            labels=labels, font_size=14,
            node_size=700, node_color=node_colors)
    plt.show()
