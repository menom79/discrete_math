import networkx as nx
import matplotlib.pyplot as plt

# Directed Graph
directed_edges = [(1, 6), (2, 3), (3, 2), (3, 4), (4, 1), (4, 3), (5, 4), (6, 7), (7, 4), (7, 5)]
G_directed = nx.DiGraph()
G_directed.add_edges_from(directed_edges)

# Undirected Graph
undirected_edges = [(1, 2), (1, 4), (2, 3), (2, 5), (2, 7), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7)]
G_undirected = nx.Graph()
G_undirected.add_edges_from(undirected_edges)

# Plot Directed Graph
plt.figure(figsize=(10, 5))
plt.subplot(121)
nx.draw(G_directed, with_labels=True, node_color='lightblue', arrows=True)
plt.title('Directed Graph')

# Plot Undirected Graph
plt.subplot(122)
nx.draw(G_undirected, with_labels=True, node_color='lightgreen')
plt.title('Undirected Graph')

# Save as an image
plt.savefig('graphs.png')
plt.show()
