from collections import deque

def breadth_first_search(graph, source, target):
    explored = set()  # Track visited nodes
    queue = deque([(source, [source])])  # Store (node, path-so-far) in the queue

    while queue:
        node, path_so_far = queue.popleft()  # Extract current node and path
        print(f"Exploring: {node}")

        if node == target:
            print(f"Success! Reached {target}.")
            print("Found Path:", " -> ".join(path_so_far))
            return True  # Stop search when target is reached

        if node not in explored:
            explored.add(node)  # Mark node as visited

            # Enqueue neighbors with their updated paths
            for neighbor in graph.get(node, []):
                if neighbor not in explored:
                    queue.append((neighbor, path_so_far + [neighbor]))

    print(f"{target} could not be reached.")
    return False  # Return False if no path to the target is found

# Define the graph with 'S' as the starting node and 'G' as the goal
graph = {
    'S': ['A', 'B'],
    'A': ['D', 'B'],
    'B': ['A', 'C'],
    'C': ['E'],  # E is a dead-end node
    'D': ['G'],
    'E': [],  # No further neighbors from E
    'G': []  # Goal node
}

# Execute the modified BFS from 'S' to 'G'
breadth_first_search(graph, 'S', 'G')
