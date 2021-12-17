import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

p1, p2 = input[0][13:].split(", ")

x1, x2 = map(int, p1[2:].split(".."))
y1, y2 = map(int, p2[2:].split(".."))

def max_y(v):
    return int(v * (v - 1) // 2)

success(max_y(abs(min(y1, y2))))
