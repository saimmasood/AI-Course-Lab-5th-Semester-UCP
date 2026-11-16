
from collections import deque

# Graph stored as a dictionary
graph = {
    'S': [('A', 3), ('C', 2), ('D', 2)],
    'A': [],
    'B': [('E', 2)],
    'C': [('F', 1)],
    'D': [('B', 3), ('G', 8)],
    'E': [('G', 2)],
    'F': [('E', 0), ('G', 4)],
    'G': []
}

def BFS(start, goal):

    queue = deque()
    queue.append((start, [start], 0))

    explored = []

    while queue:

        node, path, cost = queue.popleft()

        if node in explored:
            continue

        explored.append(node)

        if node == goal:
            return explored, path, cost

        neighbours = graph[node]

        for neighbour, weight in neighbours:

            if neighbour not in explored:

                new_path = path + [neighbour]
                new_cost = cost + weight

                queue.append((neighbour, new_path, new_cost))

    return explored, None, 0


# Define start and goal
start_node = 'S'
goal_node = 'G'

# Call BFS function
explored_order, path, total_cost = BFS(start_node, goal_node)

print("Order of nodes added to the explored set:")
print(explored_order)

print("BFS path:")
print((path))

print("Total cost:")
print(total_cost)
