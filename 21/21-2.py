import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from typing import *
from itertools import product

throws = list(product([1, 2, 3], repeat=3))

throw_sums = {}
for throw in throws:
    s = sum(throw)

    if s not in throw_sums:
        throw_sums[s] = 1
    else:
        throw_sums[s] += 1


def recursive_count(scores, positions, turn, limit=21) -> List[int]:
    universes = [0, 0]

    if scores[0] >= limit or scores[1] >= limit:
        universes[(turn + 1) % 2] = 1
        return universes

    for s in throw_sums:
        positions[turn] = (positions[turn] + s) % 10
        scores[turn] += positions[turn] + 1

        universe_delta = recursive_count(scores, positions, (turn + 1) % 2)

        universe_delta[0] *= throw_sums[s]
        universe_delta[1] *= throw_sums[s]

        universes[0] += universe_delta[0]
        universes[1] += universe_delta[1]

        scores[turn] -= positions[turn] + 1
        positions[turn] = (positions[turn] - s) % 10

    return universes


positions = list(map(lambda x: int(x[28:]) - 1, get_input()))

success(max(recursive_count([0, 0], positions, 0)))
