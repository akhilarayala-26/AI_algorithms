import random

# Graph structure with weighted edges
graph = {
    'S': {'A': 6, 'B': 5},
    'A': {'B': 5, 'D': 1},
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},
    'E': {},  # Dead end
    'G': {}   # Goal node
}

# Heuristic values representing estimated distance to the goal
heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}

def initial_greedy_path(graph, heuristic, start, end):
    """Construct a greedy initial path by choosing neighbors with minimal heuristic."""
    node = start
    path = [node]

    # Continue until the goal node is reached
    while node != end:
        neighbors = graph.get(node, {})
        if not neighbors:
            break  # Stop if no more neighbors available
        
        # Pick the neighbor with the smallest heuristic
        next_node = min(neighbors, key=lambda n: heuristic[n])
        if next_node not in path:  # Avoid cycles
            path.append(next_node)
        node = next_node

    return path

def compute_cost(heuristic, path):
    """Calculate the total path cost using heuristic values."""
    return sum(heuristic[n] for n in path)

def swap_neighbors(path):
    """Generate neighboring solutions by swapping nodes."""
    neighbors = []
    for i in range(1, len(path) - 1):  # Ignore start and goal nodes for swapping
        for j in range(i + 1, len(path) - 1):
            new_path = path[:]
            new_path[i], new_path[j] = new_path[j], new_path[i]  # Swap nodes
            neighbors.append(new_path)
    return neighbors

def find_best_neighbor(graph, heuristic, current_path):
    """Identify the best neighboring path based on cost."""
    neighbors = swap_neighbors(current_path)
    
    best_path = current_path
    lowest_cost = compute_cost(heuristic, current_path)

    for neighbor in neighbors:
        neighbor_cost = compute_cost(heuristic, neighbor)
        if neighbor_cost < lowest_cost:
            lowest_cost = neighbor_cost
            best_path = neighbor

    return best_path, lowest_cost

def hill_climb(graph, heuristic, start, end):
    """Perform the hill climbing algorithm to find an optimal path."""
    current_path = initial_greedy_path(graph, heuristic, start, end)
    current_cost = compute_cost(heuristic, current_path)

    while True:
        # Look for the best neighboring path
        neighbor_path, neighbor_cost = find_best_neighbor(graph, heuristic, current_path)

        # If no improvement, exit the loop
        if neighbor_cost >= current_cost:
            print(f"Reached a local optimum: {current_path} with cost {current_cost}")
            break

        # Move to the better neighboring path
        current_path = neighbor_path
        current_cost = neighbor_cost

    return current_path, current_cost

# Run the hill climbing algorithm
start_node = 'S'
goal_node = 'G'
final_path, final_cost = hill_climb(graph, heuristic, start_node, goal_node)

print("Optimal Path Found:", final_path)
print("Total Path Cost:", final_cost)
