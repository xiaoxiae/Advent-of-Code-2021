import sys

sys.path.insert(0, "../")
from utilities import success, get_input


def find_set(l, inverted=False):
    for i in range(len(l[0])):
        line = [l[j][i] for j in range(len(l))]
        ones = line.count("1")
        zeroes = line.count("0")

        l = list(
            filter(
                lambda x: x[i]
                == (
                    ("0" if zeroes > ones else "1")
                    if not inverted
                    else ("1" if zeroes > ones else "0")
                ),
                l,
            )
        )

        if len(l) == 1:
            return l[0]


input = get_input()

success(int(find_set(input), 2) * int(find_set(input, inverted=True), 2))
