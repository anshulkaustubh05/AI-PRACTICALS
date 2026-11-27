# Practical 1: Set up Python environment for AI and implement a simple reflex agent
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

import sys
import numpy as np
import sklearn

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 1 - Python Environment + Simple Reflex Agent")
print("-" * 55)

# checking the environment
print("Python version      :", sys.version.split()[0])
print("NumPy version       :", np.__version__)
print("Scikit-learn version:", sklearn.__version__)
print()

# Vacuum cleaner world with two rooms A and B
rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"


def reflex_agent(location, status):
    # condition - action rules
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


print("Initial rooms:", rooms, " Agent is in room", location)
for step in range(1, 7):
    status = rooms[location]
    action = reflex_agent(location, status)
    print("Step", step, ": Percept =", (location, status), "-> Action =", action)
    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    else:
        location = "A"

print()
print("Final rooms:", rooms)
