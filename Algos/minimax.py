def minimax(depth, node, maximizingPlayer, values):
    if depth == 2:
        return values[node]

    if maximizingPlayer:
        best = -9999

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, False, values)
            best = max(best, value)

        return best

    else:
        best = 9999

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, True, values)
            best = min(best, value)

        return best


values = [3, 5, 2, 9]

result = minimax(0, 0, True, values)

print("Optimal value:", result)