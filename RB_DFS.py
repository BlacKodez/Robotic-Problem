def dfs(graph, start, goal, obstacles):
    stack = [(start, [start])] # Stack to store the current node and the path
    visited = set() # Set to store visited nodes

    while stack:
        node, path = stack.pop() # Get the current node and its path

        if node == goal:
            return path # Return the path if the goal is reached

        if node not in visited:
            visited.add(node) # Mark the node as visited

            # Check the neighboring nodes
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in obstacles:
                    stack.append((neighbor, path + [neighbor])) # Add neighboring nodes to the stack with updated path

    return None # Return None if the goal is not reachable


# Define the graph as a dictionary of nodes and their neighbors
graph = {
    'S': ['OBS', '7', 'OBS'],
    '3': ['OBS', '4', 'OBS', '9', '10'],
    '4': ['3', '9', 'OBS', '10'],
    'G': ['12', 'OBS', 'OBS'],
    '7': ['S', '14', '13', 'OBS', 'OBS'],
    '9': ['OBS', 'OBS', '14', '15', '16', '10', '4', '3'],
    '10': ['OBS', 'OBS', '4', '3', '9', '15', '16', 'OBS'],
    '12': ['OBS', 'OBS', 'OBS', 'G', '18'],
    '13': ['7', 'OBS', '14', '20', '19'],
    '14': ['OBS', '7', '13', '19', '20', 'OBS', '15', '9'],
    '15': ['9', 'OBS', '14', '20', 'OBS', '22', '16', '10'],
    '16': ['10', '9', '15', 'OBS', '22', 'OBS', 'OBS', 'OBS'],
    '18': ['12', 'OBS', 'OBS', 'OBS', '24'],
    '19': ['13', '14', '20', '25', '26'],
    '20': ['14', '13', '19', '25', '26', 'OBS', 'OBS', '15'],
    '22': ['16', '15', 'OBS', 'OBS', '28', '29', 'OBS', 'OBS'],
    '24': ['18', 'OBS', 'OBS', '29', '30'],
    '25': ['19', '20', '26', '32', '31'],
    '26': ['20', '19', '25', '31', '32', 'OBS', 'OBS', 'OBS'],
    '28': ['22', 'OBS', 'OBS', 'OBS', '34', '35', '29', 'OBS'],
    '29': ['OBS', '22', '28', '34', '35', '36', '30', '24'],
    '30': ['24', 'OBS', '29', '35', '36'],
    '31': ['25', '26', '32', '37', '38'],
    '32': ['26', '25', '31', '37', '38', 'OBS', 'OBS', 'OBS'],
    '34': ['28', 'OBS', 'OBS', 'OBS', '40', '41', '35', '29'],
    '35': ['29', '28', '34', '40', '41', '42', '36', '30'],
    '36': ['30', '29', '35', '41', '42'],
    '37': ['31', '32', '38'],
    '38': ['31', '32', '37', 'OBS', 'OBS'],
    '40': ['34', '35', '41', 'OBS', 'OBS'],
    '41': ['34', '40', '35', '36', '42'],
    '42': ['36', '41', '35']
}

# Define the obstacles
obstacles = ['OBS']

# Define the start and goal nodes
start_node = 'S'
goal_node = 'G'

# Perform DFS
result = dfs(graph, start_node, goal_node, obstacles)

# Print the result
if result:
    print("Path found:", ' -> '.join(result))
else:
    print("Path not found.")
