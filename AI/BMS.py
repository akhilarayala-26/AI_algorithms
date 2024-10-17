from collections import deque

# Define the graph as an adjacency list
graph = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['E'],  
    'D': ['G'],
    'E': [],  # Dead-end
    'G': []   # Goal node
}

def bfs_search(graph, start, goal):
    """Perform BFS to find a path from start to goal."""
    queue = deque([[start]])  # Queue stores paths
    visited = set()           # Keep track of visited nodes

    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        node = path[-1]

        # If goal is found, return the path
        if node == goal:
            return path

        # If node hasn't been visited, explore neighbors
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)  # Copy current path
                new_path.append(neighbor)
                queue.append(new_path)  # Add new path to the queue

    return None  # Return None if no path is found

# Run BFS to find two paths from 'S' to 'G'
path1 = bfs_search(graph, 'S', 'G')
print("Path 1:", " -> ".join(path1) if path1 else "No path found")

# Modify graph slightly to explore another path
graph['S'] = ['B']  # Reverse order to get a different path

path2 = bfs_search(graph, 'S', 'G')
print("Path 2:", " -> ".join(path2) if path2 else "No path found")
