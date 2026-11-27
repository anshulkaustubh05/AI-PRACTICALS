# Practical 10: Value Iteration in a Grid World (MDP)
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 10 - Value Iteration on 3x4 Grid World")
print("-" * 55)

ROWS, COLS = 3, 4
wall = (1, 1)
terminals = {(0, 3): 1.0, (1, 3): -1.0}
step_reward = -0.04
gamma = 0.9
actions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
# agent goes in the chosen direction with 0.8 prob, sideways with 0.1 each
sideways = {"^": "<>", "v": "<>", "<": "^v", ">": "^v"}


def move(state, a):
    r, c = state[0] + actions[a][0], state[1] + actions[a][1]
    if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) == wall:
        return state
    return (r, c)


def q_value(V, s, a):
    total = 0.8 * V[move(s, a)]
    for side in sideways[a]:
        total += 0.1 * V[move(s, side)]
    return step_reward + gamma * total


states = [(r, c) for r in range(ROWS) for c in range(COLS) if (r, c) != wall]
V = {s: 0.0 for s in states}
for s in terminals:
    V[s] = terminals[s]

iteration = 0
while True:
    iteration += 1
    new_V = dict(V)
    delta = 0
    for s in states:
        if s in terminals:
            continue
        new_V[s] = max(q_value(V, s, a) for a in actions)
        delta = max(delta, abs(new_V[s] - V[s]))
    V = new_V
    if delta < 0.0001:
        break

print("Converged after", iteration, "iterations")
print()
print("State values:")
for r in range(ROWS):
    row = ""
    for c in range(COLS):
        if (r, c) == wall:
            row += "  WALL  "
        else:
            row += "{:7.3f} ".format(V[(r, c)])
    print("  ", row)

print()
print("Optimal policy:")
for r in range(ROWS):
    row = ""
    for c in range(COLS):
        s = (r, c)
        if s == wall:
            row += "  #"
        elif s in terminals:
            row += " +1" if terminals[s] > 0 else " -1"
        else:
            best = max(actions, key=lambda a: q_value(V, s, a))
            row += "  " + best
        row += "  "
    print("  ", row)
