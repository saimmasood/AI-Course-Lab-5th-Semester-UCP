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
    explored = []

    queue = [(cost, path)]

    while queue:
        minIndex = 0

        for i in range(len(queue)):
            currentNode = Heuristic[queue[minIndex][1][-1]]
            nextNode = Heuristic[queue[i][1][-1]]

            if currentNode > nextNode:
                minIndex = i

        cost, path = queue.pop(minIndex)

        last_explored = path[-1]

        if last_explored not in explored:
            explored.append(last_explored)

        if last_explored == goal:
            print("Order of nodes added to the explored set:", explored)
            path.append(cost)
            return path

        for n, w in myGraph[last_explored]:
            newPath = list(path)
            newPath.append(n)

            queue.append((cost + w, newPath))


print(GBFS('S', 'G', graph))