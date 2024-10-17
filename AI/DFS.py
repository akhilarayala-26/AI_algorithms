def depth_first_search(graph, current, target, explored=None, route=None):
    if explored is None:
        explored = set()  # Initialize set to track visited nodes
    if route is None:
        route = []  # Initialize list to store the current path

    explored.add(current)  # Mark the current node as explored
    route.append(current)  # Add the node to the route
    print(f"Currently at: {current}")

    # Check if the target is found
    if current == target:
        print(f"Success! Reached {target}.")
        print("Discovered Path:", " -> ".join(route))
        return True  # Stop recursion once the target is found

    # Traverse neighboring nodes recursively
    for adjacent in graph.get(current, []):
        if adjacent not in explored:
            if depth_first_search(graph, adjacent, target, explored, route):
                return True  # Goal found via this route

    route.pop()  # Backtrack by removing the last node from the route
    return False  # Return False if no path to the goal is found

# Graph with 'S' as the starting node and 'G' as the goal
graph = {
    'S': ['A', 'B'],
    'A': ['D', 'B'],
    'B': ['A', 'C'],
    'C': ['E'],  # C leads to a dead-end node E
    'D': ['G'],
    'E': [],  # No further nodes from E
    'G': []  # G is the goal node
}

# Execute DFS starting from 'S' to find 'G'
depth_first_search(graph, 'S', 'G')
