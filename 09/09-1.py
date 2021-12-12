import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

for i in range(len(input)):
    input[i] = list(map(int, list(input[i])))


def in_bounds(x, y):
    return 0 <= x < len(input[0]) and 0 <= y < len(input)


total = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        val = input[y][x]
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            if not in_bounds(nx, ny):
                continue

            if input[ny][nx] <= val:
                break
        else:
            total += 1 + val

success(total)
