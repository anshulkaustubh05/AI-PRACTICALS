# Practical 6: Constraint Satisfaction - N-Queens and Map Coloring using backtracking
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 6 - CSP: N-Queens and Map Coloring")
print("-" * 55)

# ---------- Part A : N-Queens ----------
N = 8
solutions = []


def is_safe(queens, row, col):
    # consistency check: same column or same diagonal
    for r in range(row):
        c = queens[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(queens, row):
    if row == N:
        solutions.append(queens[:])
        return
    for col in range(N):
        if is_safe(queens, row, col):
            queens.append(col)
            solve(queens, row + 1)
            queens.pop()          # backtrack


solve([], 0)
print("A) 8-Queens: total solutions =", len(solutions))
print("   First solution:")
for r in range(N):
    print("   ", " ".join("Q" if solutions[0][r] == c else "." for c in range(N)))
print()

# ---------- Part B : Map Coloring (Australia) ----------
regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
neighbours = {
    "WA": ["NT", "SA"], "NT": ["WA", "SA", "Q"], "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"], "NSW": ["Q", "SA", "V"], "V": ["SA", "NSW"], "T": []
}
colors = ["Red", "Green", "Blue"]


def consistent(region, color, assignment):
    for n in neighbours[region]:
        if assignment.get(n) == color:
            return False
    return True


def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment
    region = [r for r in regions if r not in assignment][0]
    for color in colors:
        if consistent(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]
    return None


print("B) Map Coloring of Australia:")
answer = backtrack({})
for r in regions:
    print("   ", r.ljust(4), "->", answer[r])
