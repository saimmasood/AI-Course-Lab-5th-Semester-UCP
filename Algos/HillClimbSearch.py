# Graph representation
# Each node contains the list of its neighbouring nodes
MyGraph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E'],
}

# Heuristic values h(n)
# Estimated distance from each node to the goal (smaller = closer)
HeuristicVales = {
    'A': 25,
    'B': 8,
    'C': 20,
    'D': 6,
    'E': 12,
    'F': 0,
}

# Hill Climbing Search Function
def HCS_simple(start, goal):

    Node = start  # start from the initial node

    while True:  # repeat until goal or a dead end

        print(Node)  # print the node we are standing on

        # goal test: stop if the current node is the goal
        if Node == goal:
            print('Goal Node Found...')
            break

        # assume the current node is the best so far
        minH = Node

        # look at ALL neighbours and keep the one with the
        # smallest heuristic value
        for child in MyGraph[Node]:

            if HeuristicVales[minH] > HeuristicVales[child]:
                minH = child

        # no neighbour is better than the current node:
        # we are stuck on a peak (local maximum)
        if minH == Node:
            print('Max Point.....')
            break

        Node = minH  # move to the better neighbour


# Run the algorithm
HCS_simple('A', 'F')