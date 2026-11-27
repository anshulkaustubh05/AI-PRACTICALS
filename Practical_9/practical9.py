# Practical 9: STRIPS planning for Blocks World
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

from collections import deque

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 9 - STRIPS Planning (Blocks World)")
print("-" * 55)

blocks = ["A", "B", "C"]

# initial: C is on A, A and B are on table
initial = {"On(C,A)", "OnTable(A)", "OnTable(B)", "Clear(C)", "Clear(B)", "HandEmpty"}
# goal: A on B and B on C
goal = {"On(A,B)", "On(B,C)"}


def make_actions():
    # every action = (name, preconditions, add list, delete list)
    actions = []
    for x in blocks:
        actions.append(("PickUp(" + x + ")",
                        {"Clear(" + x + ")", "OnTable(" + x + ")", "HandEmpty"},
                        {"Holding(" + x + ")"},
                        {"Clear(" + x + ")", "OnTable(" + x + ")", "HandEmpty"}))
        actions.append(("PutDown(" + x + ")",
                        {"Holding(" + x + ")"},
                        {"OnTable(" + x + ")", "Clear(" + x + ")", "HandEmpty"},
                        {"Holding(" + x + ")"}))
        for y in blocks:
            if x != y:
                actions.append(("Stack(" + x + "," + y + ")",
                                {"Holding(" + x + ")", "Clear(" + y + ")"},
                                {"On(" + x + "," + y + ")", "Clear(" + x + ")", "HandEmpty"},
                                {"Holding(" + x + ")", "Clear(" + y + ")"}))
                actions.append(("UnStack(" + x + "," + y + ")",
                                {"On(" + x + "," + y + ")", "Clear(" + x + ")", "HandEmpty"},
                                {"Holding(" + x + ")", "Clear(" + y + ")"},
                                {"On(" + x + "," + y + ")", "Clear(" + x + ")", "HandEmpty"}))
    return actions


def plan(initial, goal):
    actions = make_actions()
    queue = deque([(frozenset(initial), [])])
    visited = set()
    while queue:
        state, steps = queue.popleft()
        if goal.issubset(state):
            return steps
        if state in visited:
            continue
        visited.add(state)
        for name, pre, add, delete in actions:
            if pre.issubset(state):
                new_state = (state - delete) | add
                queue.append((frozenset(new_state), steps + [name]))
    return None


print("Initial state:", sorted(initial))
print("Goal state   :", sorted(goal))
print()
result = plan(initial, goal)
print("Plan found with", len(result), "steps:")
for i, step in enumerate(result, 1):
    print("  ", i, ".", step)
