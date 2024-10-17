import math

# Define the graph with weighted edges (costs)
graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

# Define the heuristic values (estimated cost to reach goal)
heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}

# AO* algorithm function
def ao_star(node, graph, heuristic, goal, visited):
    # If node is the goal, return 0 cost and the path as we have reached the goal
    if node == goal:
        return 0, [goal]
    
    # If node is already visited, return a high cost to avoid cycles
    if node in visited:
        return math.inf, []
    
    visited.add(node)  # Mark the node as visited
    
    min_cost = math.inf
    best_subtree_path = []

    # Explore each OR subtree from the current node
    for child_node, cost in graph[node].items():
        subtree_cost, subtree_path = ao_star(child_node, graph, heuristic, goal, visited)
        total_cost = cost + subtree_cost  # Only consider the actual edge cost and subtree cost

        # Update if a cheaper subtree is found
        if total_cost < min_cost:
            min_cost = total_cost
            best_subtree_path = [node] + subtree_path  # Add current node to the path
    
    visited.remove(node)  # Unmark the node after processing

    return min_cost, best_subtree_path

# Function to run the AO* algorithm
def run_ao_star(start_node, goal_node):
    visited = set()  # Set to track visited nodes
    total_cost, solution_path = ao_star(start_node, graph, heuristic, goal_node, visited)
    return solution_path, total_cost

# Test the AO* algorithm
start_node = 'S'
goal_node = 'G'
solution_path, total_cost = run_ao_star(start_node, goal_node)

print("AO* Solution Path:", solution_path)
print("Total Cost to Goal:", total_cost)