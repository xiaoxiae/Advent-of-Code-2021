import sys

sys.path.insert(0, "../")
from utilities import success, get_input

def is_within_bounds(v, v_min, v_max):
    """Return True if the value is within bounds."""
    return v_min <= x <= v_max


def is_on(x, y, z, commands):
    """Return True if the specified point is turned on."""
    last_status = None
    for status, xr, yr, zr, in commands:
        if is_within_bounds(x, *xr) and is_within_bounds(y, *yr) and is_within_bounds(z, *zr):
            last_status = status

    return last_status == "on"


commands_str = get_input()
commands = []

for command in commands_str:
    status, coordinates = command.split()

    xs, ys, zs = map(lambda x: x[2:], coordinates.split(","))

    f = lambda x: tuple(map(int, x.split("..")))

    commands.append((status, f(xs), f(ys), f(zs)))

total = 0
for x in range(-50, 50 + 1):
    for y in range(-50, 50 + 1):
        for z in range(-50, 50 + 1):
            if is_on(x, y, z, commands):
                total += 1

success(total)
