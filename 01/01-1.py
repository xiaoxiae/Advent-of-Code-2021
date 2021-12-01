import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input(as_int=True)

total = 0
for i in range(len(input) - 1):
    if input[i] < input[i + 1]:
        total += 1

success(total)
