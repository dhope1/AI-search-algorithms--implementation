import sets
import collections

# Creating a set to store the nodes of the graph.
nodes = set(["S", "A", "B", "C", "D", "G"])

# Creating a dictionary to store the adjacency list of the graph.
adjacency_list = collections.defaultdict(list)

# Adding the edges of the graph to the adjacency list.
adjacency_list["S"] = ["A", "B"]
adjacency_list["A"] = ["S", "B", "C"]
adjacency_list["B"] = ["S", "A", "C"]
adjacency_list["C"] = ["A", "B", "D", "G"]
adjacency_list["D"] = ["C", "G"]
adjacency_list["G"] = ["C", "D"]

# Printing the adjacency list.
print(adjacency_list)
