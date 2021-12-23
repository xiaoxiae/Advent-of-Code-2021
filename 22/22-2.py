import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from typing import *

Rectangle = Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
Command = Tuple[str, Rectangle]

Point =  Tuple[int, int, int]

def is_within_bounds(v: int, v_min: int, v_max: int):
    """Return True if the value is within bounds."""
    return v_min <= v <= v_max


def is_on(point: Point, rectangles: List[Rectangle]):
    """Return True if the specified point is turned on."""
    x, y, z = point
    last_status = None

    for status, (xr, yr, zr), in rectangles:
        if is_within_bounds(x, *xr) and is_within_bounds(y, *yr) and is_within_bounds(z, *zr):
            last_status = status

    return last_status == "on"


def get_sorted_coordinates(rectangles: List[Rectangle]):
    """Return 3 lists of the sorted coordinates of each of the rectangles."""
    xs = []
    ys = []
    zs = []

    for (x1, x2), (y1, y2), (z1, z2) in rectangles:
        xs.append(x1)
        xs.append(x2)
        ys.append(y1)
        ys.append(y2)
        zs.append(z1)
        zs.append(z2)

    return tuple(map(sorted, (xs, ys, zs)))


def get_segments(coordinates: List[int], rectangles: List[Rectangle]):
    segments = []

    for i in range(len(coordinates) - 1):
        x1, x2 = coordinates[i], coordinates[i + 1]
        if x1 == x2:
            continue

        segments.append((x1, x1))

        # if the are some things between, return them
        if x1 != x2 + 1:
            segments.append((x1 + 1, x2 - 1))

    segments.append((x2, x2))

    return segments


def count_lit_points(rectangles: List[Rectangle], commands: List[Command]):
    xs, ys, zs = get_sorted_coordinates(rectangles)

    total = 0

    xseg = get_segments(xs, rectangles)
    yseg = get_segments(ys, rectangles)
    zseg = get_segments(zs, rectangles)

    i = 1
    for x1, x2 in xseg:
        print(f"{int(i / len(xseg) * 100)} %")

        for y1, y2 in yseg:
            for z1, z2 in zseg:
                if is_on((x1, y1, z1), commands):
                    total += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
        i += 1

    return total


commands_str = get_input()

commands: List[Command] = []
rectangles: List[Rectangle] = []

for command in commands_str:
    status, coordinates = command.split()

    xs, ys, zs = map(lambda x: x[2:], coordinates.split(","))

    f = lambda x: tuple(map(int, x.split("..")))

    commands.append((status, (f(xs), f(ys), f(zs))))
    rectangles.append((f(xs), f(ys), f(zs)))

success(count_lit_points(rectangles, commands))
