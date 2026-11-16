
from collections import deque

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



def BFS(start,goal):

    queue=deque()
    node=start
    path=[start]
    cost=0

    queue.append((node,path,cost))
    explored=[]

    while queue:
        node,path,cost=queue.popleft()

        if node in explored:
            continue
        explored.append(node)

        if node ==goal:
            return explored,path,cost

        neighbour = graph[node]

        for n,w in neighbour:
            if n not in explored:
                new_path=path+[n]
                new_cost = cost+w

            queue.append((n,new_path,new_cost))

    return explored,None,0


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


        

