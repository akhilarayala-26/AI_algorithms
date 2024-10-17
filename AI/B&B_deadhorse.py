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

# Branch and Bound with Dead Horse Principle (Extended List)
def branch_and_bound_with_extended_list(graph, start, goal):
    # Priority queue (min-heap) to store paths with their cost
    queue = [(0, start, [start])]  # (cost, current_node, path)
    
    # Extended list (visited nodes with the minimum cost at which they were visited)
    extended_list = {}
    
    # Initialize the best known cost to infinity
    best_cost = float('inf')
    best_path = None
    
    while queue:
        # Pop the path with the smallest cost
        current_cost, current_node, path = heapq.heappop(queue)
        
        # If we have reached the goal and the cost is lower than the best known cost
        if current_node == goal and current_cost < best_cost:
            best_cost = current_cost
            best_path = path
        
        # Check if this node was visited with a lower or equal cost before (Dead Horse Principle)
        if current_node in extended_list and extended_list[current_node] <= current_cost:
            continue  # Skip this node as we've visited it with a better or equal cost
        
        # Update the extended list with the new minimum cost for this node
        extended_list[current_node] = current_cost
        
        # Explore neighbors of the current node
        for neighbor, edge_cost in graph[current_node].items():
            total_cost = current_cost + edge_cost
            
            # Only add the neighbor to the queue if its total cost is less than the best known cost
            if total_cost < best_cost:
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))
    
    return best_path, best_cost

# Test the Branch and Bound with Dead Horse Principle
start_node = 'S'
goal_node = 'G'

solution_path, solution_cost = branch_and_bound_with_extended_list(graph, start_node, goal_node)

print("Best Path Found (Branch and Bound with Extended List):", solution_path)
print("Total Path Cost:", solution_cost)