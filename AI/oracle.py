import heapq

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

# Function to find the least-cost path using a Dijkstra-like algorithm
def find_least_cost_oracle(graph, start, goal):
    # Priority queue (min-heap) to store the cost and path
    queue = [(0, start, [start])]  # (cost, current_node, path)
    
    # Dictionary to track the minimum cost to reach each node
    min_costs = {node: float('inf') for node in graph}
    min_costs[start] = 0
    
    while queue:
        # Pop the node with the smallest cost
        current_cost, current_node, path = heapq.heappop(queue)
        
        # If we've reached the goal, return the path and the cost
        if current_node == goal:
            return path, current_cost
        
        # Explore neighbors of the current node
        for neighbor, cost in graph[current_node].items():
            total_cost = current_cost + cost
            
            # If this path to the neighbor is cheaper, update the cost and add it to the queue
            if total_cost < min_costs[neighbor]:
                min_costs[neighbor] = total_cost
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))
    
    # Return None if no path is found
    return None, float('inf')

# Test the least-cost oracle finding method
start_node = 'S'
goal_node = 'G'

solution_path, solution_cost = find_least_cost_oracle(graph, start_node, goal_node)

print("Least Cost Oracle Path:", solution_path)
print("Total Path Cost:", solution_cost)