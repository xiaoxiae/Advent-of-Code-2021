import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from typing import *
from itertools import *

input = get_input(whole=True)

scanners = []

Coordinate = Tuple[int, int, int]
Scanner = List[Coordinate]


def get_orientations(scanner: Scanner) -> List[Scanner]:
    """Orient the scanner in all possible ways."""
    orientations = []
    for s1, s2, s3 in product((1, -1), repeat=3):
        for p in permutations((0, 1, 2)):
            orientations.append([])
            for beacon in scanner:
                x, y, z = beacon[p[0]] * s1, beacon[p[1]] * s2, beacon[p[2]] * s3
                orientations[-1].append((x, y, z))
    return orientations


def get_shifts(shifts: Scanner, scanner: Scanner) -> List[Tuple[Coordinate, Scanner]]:
    """Return all possible scanners when aligning all possible beacon pairs."""
    new_shifts = []
    for x1, y1, z1 in shifts:
        for x2, y2, z2 in scanner:
            dx, dy, dz = x1 - x2, y1 - y2, z1 - z2

            new_shifts.append([(dx, dy, dz), []])
            for x, y, z in scanner:
                new_shifts[-1][-1].append((x + dx, y + dy, z + dz))

    return new_shifts


def get_overlapping_beacons(s1: Scanner, s2: Scanner) -> int:
    """Return the overlapping beacons for the scanners."""
    total = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                total.append(s1[i])
    return total


def find_correct_orientation(
    correct_scanner, incorrect_scanner
) -> Optional[Tuple[Coordinate, Scanner]]:
    """Find the correct orientation of the incorrect scanner, given a correct one.
    Return it and the relative distance from the correct scanner."""
    for oriented_scanner in get_orientations(incorrect_scanner):
        for delta, shifted_scanner in get_shifts(correct_scanner, oriented_scanner):
            if len(get_overlapping_beacons(correct_scanner, shifted_scanner)) >= 12:
                return delta, shifted_scanner


def distance(c1: Coordinate, c2: Coordinate):
    """Return the Manhattan distance of two coordinates."""
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


for i, scanner in enumerate(input.split("\n\n")):
    beacons = scanner.splitlines()[1:]

    scanners.append([])

    for beacon in beacons:
        xs, ys, zs = beacon.split(",")
        scanners[-1].append((int(xs), int(ys), int(zs)))


# which scanners are oriented correctly
oriented = [False] * len(scanners)
oriented[0] = True

positions = [None] * len(scanners)
positions[0] = (0, 0, 0)

# set of tested correct -> incorrect pairs to speed up the algorithm
tested = set()

while not all(oriented):
    # always get one that is correctly oriented and one that is not
    for i in range(len(scanners)):
        if not oriented[i]:
            continue

        for j in range(len(scanners)):
            if oriented[j]:
                continue

            if (i, j) in tested:
                continue

            correct_scanner = scanners[i]
            incorrect_scanner = scanners[j]

            result = find_correct_orientation(correct_scanner, incorrect_scanner)

            if result is not None:
                (x, y, z), scanner = result

                oriented[j] = True
                scanners[j] = scanner

                positions[j] = (x, y, z)
            else:
                tested.add((i, j))

max_distance = 0

for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        d = distance(positions[i], positions[j])

        if d > max_distance:
            max_distance = d

success(max_distance)
