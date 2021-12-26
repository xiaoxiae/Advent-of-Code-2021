import sys

sys.path.insert(0, "../")
from utilities import success, get_input

sea = get_input()

sea = list(map(list, sea))
w, h = len(sea[0]), len(sea)

def next_cucumber_position(cucumber, x, y):
    dx, dy = {">": (1, 0), "v": (0, 1), ".": (0, 0)}[cucumber]
    nx, ny = (x + dx) % w, (y + dy) % h

    return nx, ny

def is_next_tile_free(sea, x, y):
    nx, ny = next_cucumber_position(sea[y][x], x, y)
    return sea[ny][nx] == "."

def pprint(sea):
    for line in sea:
        print("".join(line))
    print()

def next_state(sea):
    next_sea = list(map(list, sea))

    for y in range(h):
        for x in range(w):
            if sea[y][x] == ">" and is_next_tile_free(sea, x, y):
                nx, ny = next_cucumber_position(sea[y][x], x, y)

                next_sea[ny][nx] = next_sea[y][x]
                next_sea[y][x] = "."

    sea = list(map(list, next_sea))

    for y in range(h):
        for x in range(w):
            if sea[y][x] == "v" and is_next_tile_free(sea, x, y):
                nx, ny = next_cucumber_position(sea[y][x], x, y)

                next_sea[ny][nx] = next_sea[y][x]
                next_sea[y][x] = "."

    return tuple(map(tuple, next_sea))
    pprint(next_sea)


state = sea
i = 1
while True:
    new_state = next_state(state)

    if new_state == state:
        break

    state = new_state
    i +=  1

success(i)
