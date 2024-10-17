import heapq

# Define the graph with weighted edges (costs)
graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 0},  
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

# Best First Search (BFS) Algorithm with cost calculation
def best_first_search(start, goal, graph, heuristic):
    # Priority queue to store (heuristic_value, current_node, path, cumulative_cost)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start, [start], 0))
    
    # Set of visited nodes
    visited = set()
    
    while open_list:
        # Pop the node with the lowest heuristic value
        h_value, current_node, path, current_cost = heapq.heappop(open_list)
        
        # If the goal is reached, return the path and total cost
        if current_node == goal:
            return path, current_cost
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Explore the neighbors
        for neighbor, edge_cost in graph[current_node].items():
            if neighbor not in visited:
                # Calculate the new cumulative cost to the neighbor
                new_cost = current_cost + edge_cost
                # Push the neighbor to the priority queue with its heuristic value and updated path and cost
                heapq.heappush(open_list, (heuristic[neighbor], neighbor, path + [neighbor], new_cost))
    
    return None, None  # In case no path is found

# Run Best First Search
start_node = 'S'
goal_node = 'G'
solution_path, total_cost = best_first_search(start_node, goal_node, graph, heuristic)

print("Best First Search Solution Path:", solution_path)
print("Total Cost:", total_cost)