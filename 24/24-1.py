import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from itertools import product
from random import randint

instructions = get_input()

min = float("inf")
while True:
    x, y, z = 0, 0, 0

    # essentially brute-forced by hand
    #input = [randint(1, 9) for _ in range(5)] + [7, 8, 9, 6, 9, 9, 9, 9, 3]
    input = [7, 1] + [randint(1, 9) for _ in range(3)] + [1, 1, 2, 1, 6, 1, 1, 8, 1]

    abcs = [
        [1, 14, 12],
        [1, 10, 9],
        [1, 13, 8],
        [26, -8, 3],
        [1, 11, 0],
        [1, 11, 11],
        [1, 14, 10],
        [26, -11, 13],
        [1, 14, 3],
        [26, -1, 10],
        [26, -8, 10],
        [26, -5, 14],
        [26, -16, 6],
        [26, -6, 5],
    ]

    for w, (a, b, c) in zip(reversed(input), abcs):
        x = z % 26 + b

        z //= a

        x = 0 if x == w else 1

        y = 25 * x + 1

        z *= y

        y = (w + c) * x

        z += y

    if z == 0:
        input = list(reversed(input))
        print(input)
