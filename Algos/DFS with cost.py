graph = {
    'S': [('A', 3), ('C', 2), ('D', 2)],
    'A': [],
    'B': [('E', 2)],
    'C': [('F', 1)],
    'D': [('B', 3)],
    'E': [('G', 2)],
    'F': [('E', 0), ('G', 4)],
    'G': []
}


def DFS(start, goal):
    stack = []
    stack.append((start, [start], 0))

    explored = []

    while stack:
        node, path, cost = stack.pop()

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

                stack.append((neighbour, new_path, new_cost))

    return explored, None, 0


start_node = 'S'
goal_node = 'F'

explored_order, path, total_cost = DFS(start_node, goal_node)

print("Order of nodes added to the explored set:")
print(explored_order)

print("DFS path:")
print(" -> ".join(path))

print("Total cost:")
print(total_cost)