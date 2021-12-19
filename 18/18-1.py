from math import floor, ceil

import sys
from typing import *

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()


Number = List[Union[str, int]]


def reduce(number: Number):
    """Reduce a snailfish number."""
    while True:
        if explode(number):
            continue

        if split(number):
            continue

        break


def explode(number: Number) -> bool:
    """Explode a snailfish number (under the specified condition)."""
    depth = 0

    for i in range(len(number)):
        c = number[i]

        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1

        if depth == 5:
            l, r = number.pop(i + 1), number.pop(i + 1)

            number.pop(i)
            number.pop(i)
            number.insert(i, 0)

            for j in reversed(range(0, i)):
                if type(number[j]) is int:
                    number[j] += l
                    break

            for j in range(i + 1, len(number)):
                if type(number[j]) is int:
                    number[j] += r
                    break

            return True

    return False


def split(number: Number) -> bool:
    """Split a snailfish number (under the specified condition)."""
    for i in range(len(number)):
        c = number[i]

        if type(c) is int and c >= 10:
            l, r = floor(c / 2), ceil(c / 2)

            number.pop(i)
            number.insert(i, "]")
            number.insert(i, r)
            number.insert(i, l)
            number.insert(i, "[")

            return True

    return False


def from_string(string: str) -> Number:
    """Create a snailfish number from a string."""
    number = []

    num = ""
    for char in string:
        if char in ("[", "]"):
            if num != "":
                number.append(int(num))
                num = ""

            number.append(char)

        elif char == ",":
            if num != "":
                number.append(int(num))
                num = ""

        else:
            num += char

    return number


def add(n1: Number, n2: Number) -> Number:
    """Add two snailfish numbers, including their reduction."""
    number = ["["] + n1 + n2 + ["]"]
    reduce(number)
    return number


def magnitude(number: Number) -> int:
    """Return the magnitude of a snailfish number."""
    while len(number) != 1:
        for i in range(len(number) - 2):
            if type(number[i]) is int and type(number[i + 1]) is int:
                number.pop(i - 1)
                result = number.pop(i - 1) * 3 + number.pop(i - 1) * 2
                number[i - 1] = result
                break

    return number[0]


number = from_string(input[0])

for string in input[1:]:
    number = add(number, from_string(string))

success(magnitude(number))
