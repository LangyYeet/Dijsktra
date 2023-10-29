import heapq
from collections import defaultdict

def dijkstra(graph, initial_node):
    distances = {node: float('inf') for node in graph}
    distances[initial_node] = 0
    queue = [(0, initial_node)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# Příklad použití
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 6, 'D': 1},
    'C': {'A': 5, 'B': 6, 'D': 2},
    'D': {'B': 1, 'C': 2}
}

initial_node = 'A'
result = dijkstra(graph, initial_node)
print(result)
