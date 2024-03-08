import heapq
import time


class Search:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal, method_name, *args):
        start_time = time.time()
        if method_name == "BFS":
            route = self.bfs(start, goal)
        elif method_name == "DFS":
            route = self.dfs(start, goal)
        elif method_name == "ID-DFS":
            route = self.iddfs(start, goal, *args)
        elif method_name == "BEST-FIRST":
            route = self.best_first_search(start, goal)
        elif method_name == "A*":
            route = self.a_star_search(start, goal)
        else:
            raise ValueError("Invalid search method")
        if route:
            total_distance = self.calculate_distance(route)
            print(f"Route found using {method_name}: {route}")
            print(f"Total distance: {total_distance:.2f}")
            print(f"Time taken: {time.time() - start_time:.2f} seconds")
        else:
            print(f"No route found using {method_name}")

    def bfs(self, start, goal):
        queue = [(start, [start])]
        visited = set()
        while queue:
            current, path = queue.pop(0)
            visited.add(current)
            if current == goal:
                return path
            for neighbor, _ in self.graph.get_neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return None

    def dfs(self, start, goal, visited=set()):
        visited.add(start)
        if start == goal:
            return [start]
        for neighbor, _ in self.graph.get_neighbors(start):
            if neighbor not in visited:
                result = self.dfs(neighbor, goal, visited.copy())
                if result:
                    return [start] + result
        return None

    def iddfs(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            visited = set()
            result = self.dls(start, goal, depth, visited)
            if result:
                return result

