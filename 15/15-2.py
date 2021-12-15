import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from heapq import *

input = get_input()

for i in range(len(input)):
    input[i] = list(map(int, input[i]))

prev_w = len(input[0])
prev_h = len(input)

w = len(input[0]) * 5
h = len(input) * 5

start = (0, 0)
end = (w - 1, h - 1)

heap = [(0, start)]
explored = set([start])

def get(x, y):
    nx, ny = x % prev_w, y % prev_h
    cx, cy = x // prev_w, y // prev_h

    return (int(input[ny][nx]) + cx + cy - 1) % 9 + 1

while len(heap) != 0:
    d, (x, y) = heappop(heap)

    if (x, y) == end:
        success(d)

    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy

        if not(0 <= nx < w and 0 <= ny < h):
            continue

        if (nx, ny) in explored:
            continue

        heappush(heap, (d + get(nx, ny), (nx, ny)))
        explored.add((nx, ny))
