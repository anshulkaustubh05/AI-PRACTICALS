# Practical 11: Propositional logic - represent a problem and do logical inference
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

import itertools

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 11 - Propositional Logic Inference")
print("-" * 55)

# Problem: Rain or sprinkler makes the ground wet, wet ground is slippery.
symbols = ["Rain", "Sprinkler", "WetGround", "Slippery"]


def implies(p, q):
    return (not p) or q


# Knowledge base
KB_text = [
    "Rain => WetGround",
    "Sprinkler => WetGround",
    "WetGround => Slippery",
    "Rain",
]


def KB(m):
    return (implies(m["Rain"], m["WetGround"]) and
            implies(m["Sprinkler"], m["WetGround"]) and
            implies(m["WetGround"], m["Slippery"]) and
            m["Rain"])


print("Knowledge Base:")
for s in KB_text:
    print("   ", s)
print()

# 1) Truth table method (model checking)
models = []
for values in itertools.product([True, False], repeat=len(symbols)):
    m = dict(zip(symbols, values))
    if KB(m):
        models.append(m)

print("Models where KB is true:", len(models))
for m in models:
    print("   ", m)
print()

for query in ["WetGround", "Slippery", "Sprinkler"]:
    entailed = all(m[query] for m in models)
    print("Does KB entail", query.ljust(10), "?", "YES" if entailed else "NO")
print()

# 2) Forward chaining with the same rules
rules = [("Rain", "WetGround"), ("Sprinkler", "WetGround"), ("WetGround", "Slippery")]
facts = ["Rain"]
print("Forward chaining:")
added = True
while added:
    added = False
    for p, q in rules:
        if p in facts and q not in facts:
            facts.append(q)
            print("   ", p, "=>", q, " so", q, "is TRUE")
            added = True
print("Conclusions:", facts)
