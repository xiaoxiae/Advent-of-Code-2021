import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

forward = 0
depth = 0

for instruction, value in map(lambda x: x.split(), input):
    value = int(value)

    if instruction == "down":
        depth += value
    elif instruction == "up":
        depth -= value
    elif instruction == "forward":
        forward += value

success(depth * forward)
