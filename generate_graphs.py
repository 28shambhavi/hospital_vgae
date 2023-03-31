import networkx as nx
import numpy as np
# fix random seed
import random
random.seed(0)
import pdb
import matplotlib.pyplot as plt
import copy
from itertools import count
import scipy 
# create a random graph for hallways on a grid
class Hospital_Graph():
    def __init__(self, grid_size, instructions):
        self.grid_size = grid_size
        self.grid_graph = nx.grid_2d_graph(grid_size, grid_size)
        self.hospital_graph = nx.Graph()
        self.medical_role = instructions[0]
        self.specialty = instructions[1]
        self.create_hallways()
        self.calculate_hospital_nodes()
        self.add_nodes()
        # self.add_edges()

    def create_hallways(self):
        # for i inr random integer between 0 and grid_size
        seed_node = (random.randint(0, self.grid_size), random.randint(0, self.grid_size))
        self.hospital_graph.add_node(seed_node, type = 1)
        self.add_hallway_nodes(seed_node, self.grid_size)

    def add_hallway_nodes(self, node, n):    
            # new_node_options = [(node[0]+1, node[1]), (node[0]-1, node[1]), (node[0], node[1]+1), (node[0], node[1]-1)]
            # new_node = random.choice(new_node_options)
            # new_node = (node[0]+random.randint(-1,1), node[1]+ random.randint(-1,1))
            # for new_node in new_node_options:
            n -= 1
            new_node_options = [(node[0]+1, node[1]), (node[0]-1, node[1]), (node[0], node[1]+1), (node[0], node[1]-1)]
            new_node = random.choice(new_node_options)
            if self.hospital_graph.has_node(new_node) == False:
                self.hospital_graph.add_node(new_node, type = 1)
                self.hospital_graph.add_edge(node, new_node)
            else: 
                new_node = node
            if n > 0:
                self.add_hallway_nodes(new_node, n)

    def calculate_hospital_nodes(self):
        self.num_nodes_of_each_type = {}
        if self.specialty == "normal":
            self.num_nodes_of_each_type[1] = len(self.hospital_graph.nodes) # hallways
            self.num_nodes_of_each_type[2] = int(len(self.hospital_graph.nodes))*3 # wards
            self.num_nodes_of_each_type[3] = int(len(self.hospital_graph.nodes)/2) #OR
            self.num_nodes_of_each_type[4] = int(len(self.hospital_graph.nodes)/3) #admin
        # print(self.num_nodes_of_each_type)
        return self.num_nodes_of_each_type
        
    def add_nodes(self):
        all_new_nodes = {}
        all_new_nodes[1] = []
        all_new_nodes[2] = []
        all_new_nodes[3] = []
        all_new_nodes[4] = []
        for node in self.hospital_graph.nodes:
            # first = copy.deepcopy(node) if i == 0 else first
            # i += 1
            # if self.hospital_graph.nodes[node]["type"] == 1:
            new_node_options = [(node[0]+1, node[1]), (node[0]-1, node[1]), (node[0], node[1]+1), (node[0], node[1]-1)]
            for new_node in new_node_options:
                if self.hospital_graph.has_node(new_node) == False:
                    new_node_type = random.randint(2,4)
                    if len(all_new_nodes[new_node_type]) < self.num_nodes_of_each_type[new_node_type]:
                        all_new_nodes[new_node_type].append((new_node, node))
        for node_type in all_new_nodes:
            for new_node, hallway_node in all_new_nodes[node_type]:
                self.hospital_graph.add_node(new_node, type = node_type)
                self.hospital_graph.add_edge(new_node, hallway_node) 
          
    def visualize_graph(self, filename):
        pos = {point : point for point in self.hospital_graph.nodes}
        nodes = self.hospital_graph.nodes(data=False)
        self.colors = [int(self.hospital_graph.nodes[node]['type']) for node in self.hospital_graph]
        ec = nx.draw_networkx_edges(self.hospital_graph, pos, alpha=0.2)
        nc = nx.draw_networkx_nodes(self.hospital_graph, pos, nodelist=nodes,cmap=plt.cm.jet, node_color=self.colors,  node_size=500, alpha=0.8)
        filename = filename + ".png"
        # clear plot
        plt.savefig(filename)
        plt.clf()


    def evaluate_graph(self):
        # capacity = no. of wards * 2
        self.capacity = self.colors.count(2) * 2
        OR = self.colors.count(3)
        hallways = self.colors.count(1)
        admin = self.colors.count(4)
        # ratio of OR to admin 
        self.ratio_OR_to_admin = OR / admin
        # ratio of hallways to all nodes
        self.ratio_hallways_to_total = hallways / len(self.hospital_graph.nodes)
        distance_ward_to_OR = 0 # average distance from ward to OR
        distance_ward_to_admin = 0 # average distance from ward to admin
        counter_ward_to_OR = 0
        counter_ward_to_admin = 0
        list_of_nodes = list(self.hospital_graph.nodes(data=True))
        for idx, node in enumerate(list_of_nodes):
            for idx2, node2 in enumerate(list_of_nodes):
                if node[1]["type"] == 2 and node2[1]["type"] == 3:
                    distance_ward_to_OR += nx.shortest_path_length(self.hospital_graph, node[0], node2[0])
                    counter_ward_to_OR += 1
                if node[1]["type"] == 2 and node2[1]["type"] == 4:
                    distance_ward_to_admin += nx.shortest_path_length(self.hospital_graph, node[0], node2[0])
                    counter_ward_to_admin += 1

        average_distance_ward_to_OR = distance_ward_to_OR / counter_ward_to_OR
        average_distance_ward_to_admin = distance_ward_to_admin / counter_ward_to_admin
        return self.capacity, self.ratio_hallways_to_total, self.ratio_OR_to_admin, average_distance_ward_to_OR, average_distance_ward_to_admin
        # return self.capacity, self.ratio, 

    def get_graph_representation(self):
        # return an adjacency matrix and a feature matrix
        adj_matrix = nx.adjacency_matrix(self.hospital_graph)
        feature_matrix = np.zeros((len(self.hospital_graph.nodes), 4))
        for idx, node in enumerate(self.hospital_graph.nodes(data=True)):
            feature_matrix[idx, node[1]["type"]-1] = 1

        return adj_matrix, feature_matrix

def main():
    
    for i in range(5):
        graph1 = Hospital_Graph(100, [1, "normal"])   
        graph1.visualize_graph("smallgraph"+str(i)) 
        print("\nNumber of nodes: ", len(graph1.hospital_graph.nodes))
        print("Capacity",graph1.evaluate_graph()[0], "\nRatio Hallways:Total", graph1.evaluate_graph()[1],"\nRatio OR:Admin", graph1.evaluate_graph()[2],"\nAverage Distance Ward-OR", graph1.evaluate_graph()[3],"\nAverage Distance Ward-Admin", graph1.evaluate_graph()[4])
        adj1, feature1 = graph1.get_graph_representation()
        # print(adj1.todense())
        # print(feature1)
    # print("OR, hallways, admin: ", graph.evaluate_graph()[1:])
    # pos = {point : point for point in graph.hospital_graph.nodes}
    # # nx.draw(graph.hospital_graph.nodes , pos, with_labels = True)
    # groups = set(nx.get_node_attributes(graph.hospital_graph, 'type').values())
    # # mapping = dict(zip(sorted(groups), count()))
    # # print("mapping: ", mapping)
    # nodes = graph.hospital_graph.nodes(data=False)
    # # list(graph.hospital_graph.nodes(data=True))
    # colors = [int(graph.hospital_graph.nodes[node]['type']) for node in graph.hospital_graph]
    # # print("colors", colors)
    # ec = nx.draw_networkx_edges(graph.hospital_graph, pos, alpha=0.2)
    # nc = nx.draw_networkx_nodes(graph.hospital_graph, pos, nodelist=nodes,cmap=plt.cm.jet, node_color=colors,  node_size=500, alpha=0.8)
    # plt.colorbar(nc)
    # # nx.draw(graph.hospital_graph, pos, with_labels = True)
    # # plt.axis('on')
    # plt.show()

if __name__ == "__main__":
    main()