import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = list(map(int, get_input(whole=True).split(",")))

min_total = float("inf")
for level in range(min(input), max(input)):
    total = 0
    for i in range(len(input)):
        total += abs(input[i] - level)

    if total < min_total:
        min_total = total

success(min_total)
