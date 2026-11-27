# Practical 4: Tic-Tac-Toe game playing agent using Minimax and Alpha-Beta pruning
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 4 - Tic-Tac-Toe with Minimax and Alpha-Beta")
print("-" * 55)

lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
         (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
nodes = 0


def winner(b):
    for x, y, z in lines:
        if b[x] != ' ' and b[x] == b[y] == b[z]:
            return b[x]
    if ' ' not in b:
        return 'Draw'
    return None


def minimax(b, is_max):
    global nodes
    nodes += 1
    w = winner(b)
    if w == 'X':
        return 1
    if w == 'O':
        return -1
    if w == 'Draw':
        return 0
    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X' if is_max else 'O'
            scores.append(minimax(b, not is_max))
            b[i] = ' '
    return max(scores) if is_max else min(scores)


def alphabeta(b, alpha, beta, is_max):
    global nodes
    nodes += 1
    w = winner(b)
    if w == 'X':
        return 1
    if w == 'O':
        return -1
    if w == 'Draw':
        return 0
    if is_max:
        best = -10
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                best = max(best, alphabeta(b, alpha, beta, False))
                b[i] = ' '
                alpha = max(alpha, best)
                if alpha >= beta:
                    break
        return best
    else:
        best = 10
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                best = min(best, alphabeta(b, alpha, beta, True))
                b[i] = ' '
                beta = min(beta, best)
                if alpha >= beta:
                    break
        return best


def best_move(b, player):
    best_i = None
    best_score = -10 if player == 'X' else 10
    for i in range(9):
        if b[i] == ' ':
            b[i] = player
            score = alphabeta(b, -10, 10, player == 'O')
            b[i] = ' '
            if (player == 'X' and score > best_score) or (player == 'O' and score < best_score):
                best_score, best_i = score, i
    return best_i


def show(b):
    for i in range(0, 9, 3):
        print("    " + " | ".join(b[i:i + 3]))
        if i < 6:
            print("    ---------")


# 1) compare minimax and alpha-beta on the empty board
board = [' '] * 9
nodes = 0
minimax(board, True)
print("Nodes searched by Minimax    :", nodes)
nodes = 0
alphabeta(board, -10, 10, True)
print("Nodes searched by Alpha-Beta :", nodes)
print()

# 2) AI (X) vs AI (O), both using alpha-beta
board = [' '] * 9
player = 'X'
while winner(board) is None:
    move = best_move(board, player)
    board[move] = player
    print("Player", player, "plays at position", move)
    player = 'O' if player == 'X' else 'X'

print()
show(board)
print()
print("Result:", winner(board))
