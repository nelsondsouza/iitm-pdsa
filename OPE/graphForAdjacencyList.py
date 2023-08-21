import networkx as nx
import matplotlib.pyplot as plt

AList = {
    0: [2, 3, 6],
    2: [0, 3, 4],
    3: [4, 2, 0, 1],
    6: [1, 5, 0],
    1: [3, 6, 5],
    4: [2, 3, 5],
    5: [1, 4, 6]
}

# Create a graph object
G = nx.Graph()

# Add nodes and edges based on the adjacency list
for node, neighbors in AList.items():
    G.add_node(node)
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw the graph
nx.draw(G, with_labels=True, node_size=700, node_color='lightblue', font_weight='bold')
plt.show()
