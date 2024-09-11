import networkx as nx
import matplotlib.pyplot as plt

# Directed Graph
directed_edges = [(1,2),(1,3),(2,3),(2,4),(3,5),(4,5),(5,1),(5,3),(5,4)]
G_directed = nx.DiGraph()
G_directed.add_edges_from(directed_edges)



# Plot Directed Graph
plt.figure(figsize=(10, 5))
plt.subplot(121)
nx.draw(G_directed, with_labels=True, node_color='lightblue', arrows=True)
plt.title('Directed Graph')



# Save as an image
plt.savefig('graphs2.png')
plt.show()
