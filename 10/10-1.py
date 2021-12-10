import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

points = {")": 3, "]": 57, "}": 1197, ">": 25137}

total = 0
for line in input:
    parentheses = {")": "(", "]": "[", "}": "{", ">": "<"}

    stack = []
    for p in line:
        if p in parentheses:
            if stack.pop() != parentheses[p]:
                total += points[p]
                break
        else:
            stack.append(p)


success(total)
