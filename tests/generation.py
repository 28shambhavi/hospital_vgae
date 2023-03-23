import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import math

class Hospital_Graph():
    def __init__(self, capacity, role, speciality, transport, transfer):
        self.capacity = capacity
        self.role = role
        self.speciality = speciality
        self.transport = transport
        self.transfer = transfer

    def create_graph(self):
        G = nx.Graph()
        # Add nodes follow metrics

        for i in range(int(self.capacity/2)):
            G.add_node(i, type="ward")
        
        #choose a random number of SPD
        sterile_proc_dept = random.randint(1, 3)
        for i in range(int(self.capacity/2), int(self.capacity/2) + sterile_proc_dept):
            G.add_node(i, type="SPD")

        #choose a random number of ICU
        intensive_care_unit = random.randint(1, 3)
        for i in range(int(self.capacity/2) + sterile_proc_dept, int(self.capacity/2) + sterile_proc_dept + intensive_care_unit):
            G.add_node(i, type="ICU")

        #choose a random number of OR
        op_room = random.randint(int(self.capacity/4), int(self.capacity/2))
        for i in range(int(self.capacity/2) + sterile_proc_dept + intensive_care_unit, int(self.capacity/2) + sterile_proc_dept + intensive_care_unit + op_room):
            G.add_node(i, type="OR")

        
        #add edges following rules
        for n in G.nodes:
            # k = 0
            # # while k < 1:
            # if G.nodes[n]["type"] == "ward" and G.number_of_edges(n) < 4:
            #     G.add_edge(n, random.randint(1, int(G.number_of_nodes())))
            #     k += 1
            # elif G.nodes[n]["type"] == "SPD" and G.number_of_edges(n) < 3:
            #     G.add_edge(n, random.randint(1, int(G.number_of_nodes())))
            #     k += 1
            # elif G.nodes[n]["type"] == "ward" and G.number_of_edges(n) > 2:
            #     k += 1
            # elif G.nodes[n]["type"] == "SPD" and G.number_of_edges(n) >1:
            #     k += 1
            
            #each ward has upto 4 edges - connections can be to other wards, or to hallway
            #create clusters of 4 wards
            if G.nodes[n]["type"] == "ward":
                if G.number_of_edges(n) <=4:
                    G.add
        return G

    def calculate_metrics(self, G):
        metrics = {}
        # Calculate capacity
        # Calculate role
        # Calculate speciality
        # Calculate transport
        # Calculate transfer

        # Return metrics
        return metrics
    
    def refine_graph(self, G):
        # Modify nodes
        # Modify edges
        return G

def main():
    # Create a graph
    H = Hospital_Graph(100, 1, "ER", 10, "Command") 
    graph = H.create_graph()

    # Calculate metrics
    H.calculate_metrics(H)

    # Visualize the graph
    nx.draw(graph, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()