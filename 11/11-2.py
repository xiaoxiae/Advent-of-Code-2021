import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

NEIGHBOURS = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def do_step(grid) -> int:
    flashed = set()
    to_flash = []

    for x in range(len(grid[0])):
        for y in range(len(grid)):
            grid[y][x] += 1

            if grid[y][x] >= 10:
                to_flash.append((y, x))
                flashed.add((y, x))

    while len(to_flash) != 0:
        y, x = to_flash.pop()

        for dx, dy in NEIGHBOURS:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)):

                continue

            grid[ny][nx] += 1

            if grid[ny][nx] >= 10 and (ny, nx) not in flashed:
                to_flash.append((ny, nx))
                flashed.add((ny, nx))

    for (y, x) in flashed:
        grid[y][x] = 0

    return len(flashed)


grid = []

for line in input:
    grid.append(list(map(int, line)))

i = 1
while True:
    if do_step(grid) == 10 ** 2:
        break

    i += 1

success(i)
