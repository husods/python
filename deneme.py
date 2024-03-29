import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Yönlü bir graf oluştur
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (5, 2), (3, 6), (4, 7), (5, 8), (6, 9)])

# DFS uygula
visited = set()
dfs(G, 1, visited)

# Grafı çiz
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
plt.show()
