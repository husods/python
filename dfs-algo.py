import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=' ')
    visited.add(start)

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
    
# Örnek kullanım:
# Karmaşık bir graf oluştur
g = nx.Graph()
g.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (10, 11)])

# Perform DFS starting from node 1
print("DFS traversal:")
dfs(g, 1)
print(g.nodes())
g.remove_node(1)
print(nx.number_connected_components(g))
# Grafı görselleştir
pos = nx.spring_layout(g)
nx.draw(g, pos, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='gray')
plt.title("Graph Visualization")
plt.show()
