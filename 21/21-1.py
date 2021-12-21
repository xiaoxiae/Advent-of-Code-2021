import sys

sys.path.insert(0, "../")
from utilities import success, get_input

positions = list(map(lambda x: int(x[28:]) - 1, get_input()))
scores = [0, 0]

turn = 0
i = 0
while scores[0] < 1000 and scores[1] < 1000:
    for _ in range(3):
        positions[turn] += i + 1
        i += 1

    positions[turn] %= 10
    scores[turn] += positions[turn] + 1

    turn = (turn + 1) % 2

success(min(scores) * i)
