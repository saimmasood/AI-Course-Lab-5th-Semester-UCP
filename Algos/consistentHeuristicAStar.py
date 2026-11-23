# Graph representation
graph = {
    'S': {'A': 3, 'C': 2, 'D': 2},
    'A': {},
    'B': {'E': 2},
    'C': {'F': 1},
    'D': {'B': 3, 'G': 8},
    'E': {'G': 2},
    'F': {'E': 0, 'G': 4},
    'G': {}
}

# Heuristic values
Heuristic = {
    'S': 20,
    'A': 18,
    'C': 16,
    'D': 14,
    'B': 10,
    'E': 9,
    'F': 10,
    'G': 0
}


# Check heuristic consistency
consistent = True

for node in graph:
    for child, weight in graph[node].items():

        if Heuristic[node] > weight + Heuristic[child]:
            print("Inconsistent edge:", node, "->", child)
            consistent = False

if consistent:
    print("Heuristic is consistent")
else:
    print("Heuristic is inconsistent")


def A_star(startingNode, goal, myGraph):

    cost = 0
    path = [startingNode]
    visited = []

    queue = []
    queue.append((startingNode, path, cost))

    while queue:

        minIndex = 0

        for i in range(len(queue)):

            currentNode = Heuristic[queue[minIndex][0]] + queue[minIndex][2]

            nextNode = Heuristic[queue[i][0]] + queue[i][2]

            if currentNode > nextNode:
                minIndex = i

        # Remove the selected tuple
        node, path, cost = queue.pop(minIndex)

        if node in visited:
            continue

        visited.append(node)

        # Goal test
        if node == goal:
            print("Order of nodes added to the explored set:", visited)
            return path, cost

        # Expand neighbours
        for child in myGraph[node].keys():

            newPath = list(path)
            newPath.append(child)

            newCost = cost + myGraph[node][child]

            queue.append((child, newPath, newCost))


# Run the algorithm
result = A_star('S', 'G', graph)

print("A* path:")
print(" -> ".join(result[0]))

print("Total cost:")
print(result[1])






