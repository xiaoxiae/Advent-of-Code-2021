import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

points = {"(": 1, "[": 2, "{": 3, "<": 4}

scores = []
for line in input:
    parentheses = {")": "(", "]": "[", "}": "{", ">": "<"}

    stack = []
    for i, p in enumerate(line):
        if p in parentheses:
            if stack.pop() != parentheses[p]:
                break
        else:
            stack.append(p)
    else:
        subtotal = 0
        for p in reversed(stack):
            subtotal = subtotal * 5 + points[p]

        scores.append(subtotal)


success(sorted(scores)[len(scores) // 2])
