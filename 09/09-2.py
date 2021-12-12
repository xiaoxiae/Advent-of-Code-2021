import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]
basins = {}

for i in range(len(input)):
    input[i] = list(map(int, list(input[i])))


def in_bounds(x, y):
    return 0 <= x < len(input[0]) and 0 <= y < len(input)


def get_neighbours(x, y):
    n = []
    for dx, dy in neighbours:
        nx, ny = x + dx, y + dy

        if not in_bounds(nx, ny):
            continue

        n.append((nx, ny))

    return n


def is_lowpoint(x, y):
    val = input[y][x]
    for nx, ny in get_neighbours(x, y):
        if input[ny][nx] <= val:
            return False
    else:
        return True


def flow_to_lowpoint(x, y):
    while not is_lowpoint(x, y):
        val = input[y][x]
        for nx, ny in get_neighbours(x, y):
            if val > input[ny][nx]:
                x = nx
                y = ny
                break

    if (x, y) not in basins:
        basins[x, y] = 1
    else:
        basins[x, y] += 1


total = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == 9:
            continue

        flow_to_lowpoint(x, y)

v = sorted(basins.values())[-3:]

success(v[-1] * v[-2] * v[-3])
