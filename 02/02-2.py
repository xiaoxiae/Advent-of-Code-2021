import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

forward = 0
depth = 0
aim = 0

for instruction, value in map(lambda x: x.split(), input):
    value = int(value)

    if instruction == "down":
        aim += value
    elif instruction == "up":
        aim -= value
    elif instruction == "forward":
        forward += value
        depth += value * aim

success(depth * forward)
