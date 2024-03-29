import networkx as nx
import matplotlib.pyplot as plt

# Bir graph oluştur
G = nx.Graph()
H = nx.path_graph(7)
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2), (3,4), (1,5), (1,4)])

# Graph'ı görselleştir
pos = nx.spring_layout(G)  # Graph'ın düzenini belirle
#nx.draw(G, pos, with_labels=1, node_size=700, node_color='r', font_color='w', font_size=13)
nx.draw(H, with_labels=1, node_size=700, node_color='r', font_color='w', font_size=13)

# Görseli ekrana getir
print(G.nodes())