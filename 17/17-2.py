import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

p1, p2 = input[0][13:].split(", ")

x1, x2 = map(int, p1[2:].split(".."))
y1, y2 = map(int, p2[2:].split(".."))

x1, x2 = min(x1, x2), max(x1, x2)
y1, y2 = min(y1, y2), max(y1, y2)

def is_within_range(xv, yv):
    x, y = 0, 0

    while x <= x2 and y >= y1:
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True

        x += max(xv, 0)
        y += yv

        yv -= 1
        xv -= 1

    return False

total = 0
for xv in range(0, x2 + 1):
    for yv in range(-abs(y1), abs(y1)):
        if is_within_range(xv, yv):
            total += 1

success(total)
