import networkx as nx

def map_label_to_color(label):
    label_lc = label.lower()
    if label_lc == 'el':
        return '#ff0000'
    elif label_lc == 'i':
        return '#ffa500'
    elif label_lc == 'e':
        return '#5e90d7'
    return '#c1c1c1'

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