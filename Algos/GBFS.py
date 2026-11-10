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


def GBFS(startingNode, goal, myGraph):
    cost = 0
    path = [startingNode]
    visited = []

    queue = [(cost, path)]

    while queue:
        minIndex = 0

        for i in range(len(queue)):
            currentNode = Heuristic[queue[minIndex][1][-1]]
            nextNode = Heuristic[queue[i][1][-1]]

            if currentNode > nextNode:
                minIndex = i

        cost, path = queue.pop(minIndex)

        last_visited = path[-1]

        if last_visited not in visited:
            visited.append(last_visited)

        if last_visited == goal:
            print("Order of nodes added to the explored set:", visited)
            path.append(cost)
            return path

        for child, edgeCost in myGraph[last_visited]:
            newPath = list(path)
            newPath.append(child)

            queue.append((cost + edgeCost, newPath))


print(GBFS('S', 'G', graph))