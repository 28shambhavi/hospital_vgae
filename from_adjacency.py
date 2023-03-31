import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

adjacency_matrix = np.array([[0,1,1,0,0,1],
                            [1,0,0,1,0,0],
                            [1,0,0,0,1,0],
                            [0,1,0,0,1,0],
                            [0,0,1,1,0,1],
                                    [1,0,0,0,1,0]])

#let us have four types of nodes - ward, hallway, SPD, OR
#find minimum vertex cover and set the nodes in the cover to be of type hallway

feature_matrix = np.array([[1,0,0,1,1,0],
                            [0,1,0,0,0,0],
                            [0,0,1,0,0,0],
                            [0,0,0,0,0,1]])

G = nx.from_numpy_matrix(adjacency_matrix)
mapping = {}
pos = nx.planar_layout(G)
#create a dictionary of node type for each node
node_type = {0 : "ward", 1 : "hallway", 2 : "SPD", 3 : "OR"}

for i,j in enumerate(feature_matrix):
    for k in range(len(j)):
        if j[k] == 1:
            mapping[k] = node_type[i]

nx.set_node_attributes(G, mapping, "type")

# find the minimum number of nodes that are connected to all other nodes
# this is the minimum vertex cover
# the nodes in the vertex cover are the nodes that are of type hallway

print(nx.minimum_node_cut(G))

#show grid of positions
nx.draw(G, pos, with_labels = True)

plt.show()
# fig, ax = plt.subplots()
# nx.draw(G, pos=pos, node_color='k', ax=ax)
# nx.draw(G, pos=pos, node_size=1500, ax=ax)  # draw nodes and edges
# nx.draw_networkx_labels(G, pos=pos)  # draw node labels/names
# # draw edge weights
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
# plt.axis("on")
# ax.set_xlim(-2, 2)
# ax.set_ylim(-2,2)
# ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
# plt.show()