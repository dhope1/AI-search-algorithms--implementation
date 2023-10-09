import collections

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def depth_first_search(self, start_node, goal_node):
        visited = set()
        stack = [start_node]
        while stack:
            node = stack.pop()
            visited.add(node)
            if node == goal_node:
                return visited
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return None

    def breadth_first_search(self, start_node, goal_node):
        visited = set()
        queue = [start_node]
        while queue:
            node = queue.pop(0)
            visited.add(node)
            if node == goal_node:
                return visited
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return None

    def uniform_cost_search(self, start_node, goal_node, cost_function):
        visited = set()
        priority_queue = [(0, start_node)]
        while priority_queue:
            cost, node = priority_queue.pop(0)
            visited.add(node)
            if node == goal_node:
                return visited
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    new_cost = cost + cost_function(node, neighbor)
                    priority_queue.append((new_cost, neighbor))
        return None

    def greedy_search(self, start_node, goal_node, heuristic_function):
        visited = set()
        current_node = start_node
        while current_node != goal_node:
            visited.add(current_node)
            neighbors = self.graph[current_node]
            best_neighbor = None
            best_heuristic_value = None
            for neighbor in neighbors:
                if neighbor not in visited:
                    heuristic_value = heuristic_function(neighbor)
                    if best_neighbor is None or heuristic_value < best_heuristic_value:
                        best_neighbor = neighbor
                        best_heuristic_value = heuristic_value
            if best_neighbor is None:
                return None
            current_node = best_neighbor
        return visited

    def a_star_search(self, start_node, goal_node, cost_function, heuristic_function):
        visited = set()
        priority_queue = [(0, start_node)]
        while priority_queue:
            cost, node = priority_queue.pop(0)
            visited.add(node)
            if node == goal_node:
                return visited
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    new_cost = cost + cost_function(node, neighbor)
                    priority = new_cost + heuristic_function(neighbor)
                    priority_queue.append((priority, neighbor))
        return None

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("S", "A")
    graph.add_edge("S", "B")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")
    graph.add_edge("C", "G")
    graph.add_edge("D", "G")

    start_node = "S"
    goal_node = "G"

    # Depth First Search (DFS)
    dfs_result = graph.depth_first_search(start_node, goal_node)
    if dfs_result:
        print("DFS - Order in which states are expanded:", sorted(dfs_result))
        print("DFS - Path returned by graph search:", [start_node] + sorted(dfs_result - {start_node}))
        print("DFS - States that are not expanded:", sorted(set(graph.graph.keys()) - dfs_result))
    else:
        print("DFS: Goal node not reached.")

    # Breadth First Search (BFS)
    bfs_result = graph.breadth_first_search(start_node, goal_node)
    if bfs_result:
        print("BFS - Order in which states are expanded:", sorted(bfs_result))
        print("BFS - Path returned by graph search:", [start_node] + sorted(bfs_result - {start_node}))
        print("BFS - States that are not expanded:", sorted(set(graph.graph.keys()) - bfs_result))
    else:
        print("BFS: Goal node not reached.")

    # Uniform Cost Search (UCS)
    ucs_result = graph.uniform_cost_search(start_node, goal_node, cost_function=lambda node1, node2: 1)
    if ucs_result:
        print("UCS - Order in which states are expanded:", sorted(ucs_result))
        print("UCS - Path returned by graph search:", [start_node] + sorted(ucs_result - {start_node}))
        print("UCS - States that are not expanded:", sorted(set(graph.graph.keys()) - ucs_result))
    else:
        print("UCS: Goal node not reached.")

    # Greedy Search
    greedy_search_result = graph.greedy_search(start_node, goal_node, heuristic_function=lambda node: 1)
    if greedy_search_result:
        print("Greedy Search - Order in which states are expanded:", sorted(greedy_search_result))
        print("Greedy Search - Path returned by graph search:", [start_node] + sorted(greedy_search_result - {start_node}))
        print("Greedy Search - States that are not expanded:", sorted(set(graph.graph.keys()) - greedy_search_result))
    else:
        print("Greedy Search: Goal node not reached.")

    # A* Search
    a_star_search_result = graph.a_star_search(start_node, goal_node, cost_function=lambda node1, node2: 1, heuristic_function=lambda node: 1)
    if a_star_search_result:
        print("A* Search - Order in which states are expanded:", sorted(a_star_search_result))
        print("A* Search - Path returned by graph search:", [start_node] + sorted(a_star_search_result - {start_node}))
        print("A* Search - States that are not expanded:", sorted(set(graph.graph.keys()) - a_star_search_result))
    else:
        print("A* Search: Goal node not reached.")
