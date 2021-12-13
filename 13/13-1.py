import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input(whole=True)

dots_str, folds_str = input.split("\n\n")

dots = []
for dot in dots_str.splitlines():
    x, y = dot.split(",")
    dots.append([int(x), int(y)])

for fold in folds_str.splitlines():
    coord, val_str = fold[11:].split("=")
    val = int(val_str)

    for i in range(len(dots)):
        x, y = dots[i]

        if coord == "x":
            if x > val:
                dots[i][0] -= (x - val) * 2
        if coord == "y":
            if y > val:
                dots[i][1] -= (y - val) * 2

    break

success(len(set(map(tuple, dots))))
