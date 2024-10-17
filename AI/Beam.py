import heapq

# Graph representation with edge weights
graph = {
    'S': {'A': 6, 'B': 5},
    'A': {'B': 5, 'D': 1},
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},
    'E': {},  # E is a dead-end
    'G': {}   # Goal node
}

# Heuristic values estimate the distance to the goal node
heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}

def successors(graph, node):
    """Return the neighboring nodes of a given node."""
    return graph.get(node, {}).keys()

def beam_search_limited(graph, heuristic, start, goal, width=2):
    """Perform beam search with a fixed beam width."""
    # Initialize the beam with the start node
    beam = [(heuristic[start], [start])]  # (estimated cost, path taken so far)

    while beam:
        new_beam = []  # Store potential next steps

        # Process each path currently in the beam
        for cost, path in beam:
            current = path[-1]  # Get the last node in the path
            
            # If the goal is reached, return the path and cost
            if current == goal:
                return path, cost
            
            # Expand neighbors of the current node
            for neighbor in successors(graph, current):
                if neighbor not in path:  # Avoid revisiting nodes
                    updated_path = path + [neighbor]
                    updated_cost = cost + heuristic[neighbor]  # Heuristic-based cost
                    
                    # Add new path to the next iteration of the beam
                    new_beam.append((updated_cost, updated_path))
        
        # Retain only the top `width` paths with the lowest cost
        beam = heapq.nsmallest(width, new_beam, key=lambda x: x[0])
    
    # If the goal cannot be reached, return failure
    return None, float('inf')

# Test the modified beam search algorithm
start_node = 'S'
goal_node = 'G'
solution_path, path_cost = beam_search_limited(graph, heuristic, start_node, goal_node, width=2)

print("Beam Search Solution Path:", solution_path)
print("Beam Search Path Cost:", path_cost)
