import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input(as_int=True)

total = 0
n = 3
for i in range(len(input) - n):
    if sum(input[i : i + n]) < sum(input[i + 1 : i + n + 1]):
        total += 1

success(total)
