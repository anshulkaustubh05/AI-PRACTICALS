# Practical 3: A* search for 8-puzzle and effect of different heuristics
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

import heapq

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 3 - A* Search on 8-Puzzle")
print("-" * 55)

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)      # 0 means blank
start = (4, 1, 2, 0, 8, 7, 6, 3, 5)


def h_zero(state):
    return 0                             # no heuristic (same as UCS)


def h_misplaced(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


def h_manhattan(state):
    dist = 0
    for i in range(9):
        if state[i] != 0:
            g = goal.index(state[i])
            dist += abs(i // 3 - g // 3) + abs(i % 3 - g % 3)
    return dist


def neighbours(state):
    result = []
    b = state.index(0)
    r, c = b // 3, b % 3
    moves = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
    for m, (dr, dc) in moves.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            s = list(state)
            s[b], s[nr * 3 + nc] = s[nr * 3 + nc], s[b]
            result.append((m, tuple(s)))
    return result


def astar(start, h):
    pq = [(h(start), 0, start, [])]
    visited = set()
    expanded = 0
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal:
            return path, expanded
        if state in visited:
            continue
        visited.add(state)
        expanded += 1
        for move, nxt in neighbours(state):
            if nxt not in visited:
                heapq.heappush(pq, (g + 1 + h(nxt), g + 1, nxt, path + [move]))
    return None, expanded


def show(state):
    for i in range(0, 9, 3):
        print("   ", " ".join(str(x) if x != 0 else "_" for x in state[i:i + 3]))


print("Start state:")
show(start)
print("Goal state:")
show(goal)
print()

print("Heuristic            Moves   Nodes expanded")
for name, h in [("h0 = 0 (no info)", h_zero), ("h1 = misplaced", h_misplaced),
                ("h2 = manhattan", h_manhattan)]:
    path, expanded = astar(start, h)
    print(name.ljust(20), str(len(path)).ljust(7), expanded)

print()
print("Solution (blank moves):", " ".join(path))
print("Manhattan distance expands the fewest nodes, so it is the best heuristic.")
