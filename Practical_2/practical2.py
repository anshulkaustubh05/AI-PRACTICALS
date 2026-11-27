# Practical 2: BFS, DFS and Uniform Cost Search on a graph and compare them
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

import heapq
from collections import deque

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 2 - BFS vs DFS vs UCS")
print("-" * 55)

# weighted graph (node : {neighbour : cost})
graph = {
    'S': {'A': 1, 'B': 5},
    'A': {'D': 9, 'C': 3},
    'B': {'G': 9},
    'C': {'E': 2},
    'D': {'G': 2},
    'E': {'G': 3},
    'G': {}
}
start = 'S'
goal = 'G'


def path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost = cost + graph[path[i]][path[i + 1]]
    return cost


def bfs(start, goal):
    queue = deque([[start]])
    visited = []
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path, len(visited)
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                queue.append(path + [n])
    return None, len(visited)


def dfs(start, goal):
    stack = [[start]]
    visited = []
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path, len(visited)
        if node not in visited:
            visited.append(node)
            for n in reversed(list(graph[node])):
                stack.append(path + [n])
    return None, len(visited)


def ucs(start, goal):
    pq = [(0, [start])]
    visited = []
    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]
        if node == goal:
            return path, len(visited)
        if node not in visited:
            visited.append(node)
            for n, c in graph[node].items():
                heapq.heappush(pq, (cost + c, path + [n]))
    return None, len(visited)


print("Graph edges:")
for node in graph:
    for n, c in graph[node].items():
        print("  ", node, "->", n, " cost =", c)
print()

print("Algorithm    Path                     Cost   Nodes expanded")
for name, func in [("BFS", bfs), ("DFS", dfs), ("UCS", ucs)]:
    path, expanded = func(start, goal)
    print(name.ljust(12), " -> ".join(path).ljust(24), str(path_cost(path)).ljust(6), expanded)

print()
print("BFS finds the path with fewest edges, DFS finds any path,")
print("UCS always finds the path with the lowest cost.")
