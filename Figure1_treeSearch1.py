import collections
import heapq

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self, node1, node2, cost):
        self.graph[node1].append((node2, cost))
        self.graph[node2].append((node1, cost))

def dfs(graph, start_node, goal_node):
    stack = [(start_node, [start_node])]  # Use a stack to simulate tree search
    visited = set()

    while stack:
        node, path = stack.pop()

        if node not in visited:
            visited.add(node)

            if node == goal_node:
                return visited, path

            for neighbor, _ in graph.graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return visited, None  # If goal not found

def bfs(graph, start_node, goal_node):
    queue = collections.deque([(start_node, [start_node])])  # Use a queue for BFS
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            visited.add(node)

            if node == goal_node:
                return visited, path

            for neighbor, _ in graph.graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return visited, None  # If goal not found

def ucs(graph, start_node, goal_node):
    priority_queue = [(0, start_node, [start_node])]  # Use a priority queue for UCS
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node not in visited:
            visited.add(node)

            if node == goal_node:
                return visited, path

            for neighbor, edge_cost in graph.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return visited, None  # If goal not found

def greedy_search(graph, start_node, goal_node, heuristic_function):
    priority_queue = [(heuristic_function(start_node), start_node, [start_node])]  # Use a priority queue for Greedy Search
    visited = set()

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)

        if node not in visited:
            visited.add(node)

            if node == goal_node:
                return visited, path

            for neighbor, _ in graph.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic_function(neighbor), neighbor, path + [neighbor]))

    return visited, None  # If goal not found

def a_star_search(graph, start_node, goal_node, heuristic_function):
    priority_queue = [(heuristic_function(start_node), 0, start_node, [start_node])]  # Use a priority queue for A* Search
    visited = set()

    while priority_queue:
        _, cost, node, path = heapq.heappop(priority_queue)

        if node not in visited:
            visited.add(node)

            if node == goal_node:
                return visited, path

            for neighbor, edge_cost in graph.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic_function(neighbor) + cost + edge_cost, cost + edge_cost, neighbor, path + [neighbor]))

    return visited, None  # If goal not found

# Example usage:

graph = Graph()
graph.add_edge("S", "A", 1)
graph.add_edge("S", "B", 2)
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 5)
graph.add_edge("B", "C", 3)
graph.add_edge("C", "D", 2)
graph.add_edge("C", "G", 3)
graph.add_edge("D", "G", 1)

start_node = "S"
goal_node = "G"

# Define heuristic function for Greedy Search and A* Search (in this case, use a simple distance function)
heuristic_function = lambda node: abs(ord(node) - ord(goal_node))

# Perform searches
dfs_result, dfs_path = dfs(graph, start_node, goal_node)
bfs_result, bfs_path = bfs(graph, start_node, goal_node)
ucs_result, ucs_path = ucs(graph, start_node, goal_node)
greedy_search_result, greedy_search_path = greedy_search(graph, start_node, goal_node, heuristic_function)
a_star_search_result, a_star_search_path = a_star_search(graph, start_node, goal_node, heuristic_function)

# Print the results
print("DFS:")
print("Order in which states are expanded:", dfs_result)
print("Path returned by tree search:", dfs_path)
print("States that are not expanded:", set(graph.graph.keys()) - dfs_result)

print("\nBFS:")
print("Order in which states are expanded:", bfs_result)
print("Path returned by tree search:", bfs_path)
print("States that are not expanded:", set(graph.graph.keys()) - bfs_result)

print("\nUCS:")
print("Order in which states are expanded:", ucs_result)
print("Path returned by tree search:", ucs_path)
print("States that are not expanded:", set(graph.graph.keys()) - ucs_result)

print("\nGreedy Search:")
print("Order in which states are expanded:", greedy_search_result)
print("Path returned by tree search:", greedy_search_path)
print("States that are not expanded:", set(graph.graph.keys()) - greedy_search_result)

print("\nA* Search:")
print("Order in which states are expanded:", a_star_search_result)
print("Path returned by tree search:", a_star_search_path)
print("States that are not expanded:", set(graph.graph.keys()) - a_star_search_result)

