import matplotlib.pyplot as plt
import networkx as nx
# create number for each group to allow use of colormap
from itertools import count
import numpy as np
# get unique groups
adjacency_matrix = np.array([[0,1,0,0,1,0],
                            [0,0,1,0,0,1],
                            [0,0,1,0,0,1],
                            [0,1,0,0,0,1],
                            [1,0,0,0,0,0],
                            [0,1,1,1,0,0]])

#let us have four types of nodes - ward, hallway, SPD, OR

feature_matrix = np.array([[1,0,0,1,1,0],
                            [0,1,0,0,0,0],
                            [0,0,1,0,0,0],
                            [0,0,0,0,0,1]])

g = nx.from_numpy_matrix(adjacency_matrix)
groups = set(nx.get_node_attributes(g,'group').values())
mapping = dict(zip(sorted(groups),count()))
nodes = g.nodes()
colors = [mapping[g.nodes[n]['group']] for n in nodes]

# drawing nodes and edges separately so we can capture collection for colobar
pos = nx.spring_layout(g)
ec = nx.draw_networkx_edges(g, pos, alpha=0.2)
nc = nx.draw_networkx_nodes(g, pos, nodelist=nodes, node_color=colors, node_size=100, cmap=plt.cm.jet)
plt.colorbar(nc)
plt.axis('off')
plt.show()
