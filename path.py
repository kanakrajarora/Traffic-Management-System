import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges with weights (distance)
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1),
    ('D', 'E', 3),
    ('C', 'E', 2)
]

G.add_weighted_edges_from(edges)

# Function to find the shortest path
def find_shortest_path(graph, start, end):
    return nx.shortest_path(graph, source=start, target=end, weight='weight')

# Example usage
start_node = 'A'
end_node = 'E'
shortest_path = find_shortest_path(G, start_node, end_node)
print(f'Shortest path from {start_node} to {end_node}: {shortest_path}')

# Visualize the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))

# Draw the entire graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)

# Highlight the shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='orange', width=4)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title('Map Graph with Shortest Path Highlighted')
plt.show()
