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


def UniformCostSearch(startingNode, goal):
    cost = 0
    path = [startingNode]
    explored = []

    queue = [(cost, path)]

    while queue:
        minIndex = 0

        for i in range(len(queue)):
    
            if queue[i][0] < queue[minIndex][0]:
                minIndex = i


        cost, path = queue.pop(minIndex)

        last_explored = path[-1]

        if last_explored not in explored:
            explored.append(last_explored)

        if last_explored == goal:
            print("Order of nodes added to the explored set:", explored)
            path.append(cost)
            return path

        for neighbour, weight in graph[last_explored]:
            # newPath = path.copy()
            # newPath.append(neighbour)

            newPath=path+[neighbour]

            queue.append((cost + weight, newPath))
    

print(UniformCostSearch('S', 'G'))