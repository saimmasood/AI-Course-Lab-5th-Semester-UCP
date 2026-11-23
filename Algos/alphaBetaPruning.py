def minimax(depth, node, maximizingPlayer, values, alpha, beta):
    if depth == 2:
        return values[node]

    if maximizingPlayer:
        best = -9999

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 9999

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 2, 9]

result = minimax(0, 0, True, values, -9999, 9999)

print("Optimal value:", result)