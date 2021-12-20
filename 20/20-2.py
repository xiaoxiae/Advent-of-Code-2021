import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from typing import *

Coordinate = Tuple[int, int]
Image = Dict[Coordinate, str]
Algorithm = str


def yield_change_coordinates(image: Image) -> Generator[Coordinate, None, None]:
    """Yield all coordinates that could possibly change in this iteration."""
    coordinates = set()
    d = 1
    for x, y in image:
        for dx in range(-d, d + 1):
            for dy in range(-d, d + 1):
                coordinates.add((x + dx, y + dy))

    for coordinate in coordinates:
        yield coordinate


def get_default_value(phase, algorithm):
    """Return the default value, which is 0 by default (if the algorithm doesn't flip
    all values each iteration) and otherwise phase % 2."""
    return 0 if algorithm[0] == "." else phase % 2


def get_next_pixel_value(
    coordinate: Coordinate, image: Image, algorithm: Algorithm, phase: int
):
    """Return the value of what the next value of the coordinate should be, given the
    phase."""
    x, y = coordinate

    pixel_string = ""
    for dy in range(-1, 1 + 1):
        for dx in range(-1, 1 + 1):
            c = (x + dx, y + dy)

            if c not in image:
                value = get_default_value(phase, algorithm)
            else:
                value = 0 if image[c] == "." else 1

            pixel_string += str(value)

    return algorithm[int(pixel_string, 2)]


def get_next_image(image: Image, algorithm: Algorithm, phase: int):
    """Get the next image, given the algorithm and the current phase (if the algorithm
    flips pixel each time, we need to know the default value of a pixel)."""
    new_image = {}

    for coordinate in yield_change_coordinates(image):
        new_image[coordinate] = get_next_pixel_value(
            coordinate, image, algorithm, phase
        )

    return new_image


input = get_input(whole=True)

algorithm, image_string = input.split("\n\n")

image_string = image_string.splitlines()

# only save the coordinates of non-zero pixels
image = {}

for y in range(len(image_string)):
    for x in range(len(image_string[0])):
        image[(x, y)] = image_string[y][x]

for i in range(50):
    image = get_next_image(image, algorithm, i)

total = 0
for c in image:
    if image[c] == "#":
        total += 1
success(total)
