import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = list(map(lambda x: x.split(" -> "), get_input()))

for i in range(len(input)):
    input[i] = list(map(lambda x: list(map(int, x.split(","))), input[i]))

def get_pipe_points(x1, y1, x2, y2):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    points = []

    if x1 == x2:
        for i in range(y1, y2 + 1):
            points.append((x1, i))
    elif y1 == y2:
        for i in range(x1, x2 + 1):
            points.append((i, y1))
    else:
        print("Should not have happened.")
        quit()

    return points


point_counts = {}
for (x1, y1), (x2, y2) in input:
    if x1 == x2 or y1 == y2:
        for point in yield_pipe_points(x1, y1, x2, y2):
            if point not in point_counts:
                point_counts[point] = 1
            else:
                point_counts[point] += 1

total = 0
for point in point_counts:
    if point_counts[point] >= 2:
        total += 1

success(total)
