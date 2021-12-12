import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

caves = {}


def is_small(x):
    return x == x.lower()


for u, v in map(lambda x: x.split("-"), input):
    if u not in caves:
        caves[u] = []
    if v not in caves:
        caves[v] = []

    caves[u].append(v)
    caves[v].append(u)


total = 0


def count_distinct_paths(current, visited, repeated=False):
    global total

    if current == "end":
        total += 1
        return

    for neighbour in caves[current]:
        if neighbour == "start":
            continue

        if neighbour in visited:
            if not repeated:
                count_distinct_paths(neighbour, visited, repeated=True)
            continue

        if is_small(neighbour):
            visited.add(neighbour)

        count_distinct_paths(neighbour, visited, repeated)

        if is_small(neighbour):
            visited.remove(neighbour)


count_distinct_paths("start", set())

success(total)
