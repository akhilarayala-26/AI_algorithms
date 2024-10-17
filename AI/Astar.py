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

def a_star(graph, heuristic, start, goal):
    # Priority queue to store (f_cost, g_cost, current_node, path)
    queue = [(heuristic[start], 0, start, [start])]
    
    # Dictionary to track the cost to reach each node
    visited = {}
    
    while queue:
        # Pop the node with the lowest f(n) value
        f_cost, current_cost, current_node, path = heapq.heappop(queue)
        
        # If we've reached the goal, return the solution
        if current_node == goal:
            return path, current_cost
        
        # If this node has already been visited with a lower cost, skip it
        if current_node in visited and visited[current_node] <= current_cost:
            continue
        
        # Mark this node as visited
        visited[current_node] = current_cost
        
        # Explore the neighbors of the current node
        for neighbor, edge_cost in graph[current_node].items():
            total_cost = current_cost + edge_cost  # g(n)
            f_neighbor_cost = total_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
            
            # Add the neighbor to the queue
            heapq.heappush(queue, (f_neighbor_cost, total_cost, neighbor, path + [neighbor]))
    
    return None, float('inf')  # If no path is found

# Test the A* algorithm
start_node = 'S'
goal_node = 'G'

solution_path, solution_cost = a_star(graph, heuristic, start_node, goal_node)

print("A* Algorithm Solution Path:", solution_path)
print("Total Path Cost:", solution_cost)