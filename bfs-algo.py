import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs_visualize(graph, start):
    G = nx.Graph(graph)

    visited = set()
    queue = deque([start])

    pos = nx.spring_layout(G)  # Grafı düzgün bir şekilde yerleştir

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)

            # Grafın renklerini belirle
            node_colors = ['red' if n == node else 'lightblue' for n in G.nodes]

            # Grafı çiz
            nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', font_weight='bold')
            plt.title(f"BFS - Gezilen Node: {node}")
            plt.show(block=False)
            plt.pause(0.8)
            plt.clf()  # Mevcut grafiği temizle

            # Komşuları kuyruğa ekle
            queue.extend(graph[node])

# Örnek bir graf
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# BFS başlangıç noktası
start_node = 'A'

# BFS'yi görselleştir
bfs_visualize(graph, start_node)
