import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from heap import build_heap, get_degrees, get_heap
adjacency_matrix = np.array([[0,1,0,0,1,0],
                            [0,0,1,0,0,1],
                            [0,0,1,0,0,1],
                            [0,1,0,0,0,1],
                            [1,0,0,0,0,0],
                            [0,1,1,1,0,0]])

#let us have four types of nodes - ward, hallway, SPD, OR
#find minimum vertex cover and set the nodes in the cover to be of type hallway

feature_matrix = np.array([[1,0,0,1,1,0],
                            [0,1,0,0,0,0],
                            [0,0,1,0,0,0],
                            [0,0,0,0,0,1]])

G = nx.from_numpy_matrix(adjacency_matrix)
mapping = {}

#create a dictionary of node type for each node
node_type = {0 : "ward", 1 : "hallway", 2 : "SPD", 3 : "OR"}

for i,j in enumerate(feature_matrix):
    for k in range(len(j)):
        if j[k] == 1:
            mapping[k] = node_type[i]

print(mapping)
nx.set_node_attributes(G, mapping, "type")


nx.draw(G, with_labels=True)
plt.show()