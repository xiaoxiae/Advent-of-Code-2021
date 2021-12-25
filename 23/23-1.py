import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from typing import *
from heapq import *

Diagram = List[List[str]]
Amphipod = str

diagram = get_input()

for i in range(len(diagram)):
    diagram[i] = list(diagram[i])

    while i != 0 and len(diagram[i]) != len(diagram[i - 1]):
        diagram[i].append(" ")


states = []


def is_room(x: int, y: int) -> bool:
    """Return True if the given coordinate is inside a room."""
    return y in (2, 3) and x in (3, 5, 7, 9)


def is_hallway(x: int, y: int) -> bool:
    """Return True if the given coordinate is inside the hallway."""
    return y == 1 and x in range(1, 12)


def is_outside_room(x: int, y: int) -> bool:
    """Return True if the given coordinate is just outside the room."""
    return y == 1 and x in (3, 5, 7, 9)


def is_free(x: int, y: int, diagram: Diagram) -> bool:
    """Return True if no amphipod occupies the specified coordinate."""
    return diagram[y][x] == "."


def is_correct_room(amphipod: Amphipod, x: int, y: int):
    """Return True if this is the amphipod's correct room."""
    return (
        (amphipod == "A" and x == 3)
        or (amphipod == "B" and x == 5)
        or (amphipod == "C" and x == 7)
        or (amphipod == "D" and x == 9)
    )


def can_move_to(
    amphipod: Amphipod, x: int, y: int, xn: int, yn: int, diagram: Diagram
) -> bool:
    """Return True if an amphipod can move to the position (assuming it's empty."""
    # can never move to outside the room
    if is_outside_room(xn, yn):
        return False

    # can move to the correct room (but not to block the entrance)
    if is_correct_room(amphipod, xn, yn):
        if diagram[yn][xn] == "." or is_correct_room(xn, yn + 1, diagram):
            return True
        return False

    # can move to the hallway, only if it's not in it already
    if is_hallway(xn, yn) and not is_hallway(x, y):
        return True

    return False


def reachable_positions(x: int, y: int, diagram: Diagram) -> Dict[int, Tuple[int, int]]:
    """Return positions reachable from the given x, y, accounting for other amphipods."""
    reachable = {}
    stack = [(0, x, y)]

    while len(stack) != 0:
        d, x, y = heappop(stack)

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            xn = x + dx
            yn = y + dy

            if is_free(xn, yn, diagram) and (xn, yn) not in reachable:
                heappush(stack, (d + 1, xn, yn))
                reachable[(xn, yn)] = d + 1

    return reachable


def move_cost(amphipod):
    return {"A": 1, "B": 10, "C": 100, "D": 1000}[amphipod]


def is_correct(diagram):
    return (
        diagram[2][3] == "A"
        and diagram[3][3] == "A"
        and diagram[2][5] == "B"
        and diagram[3][5] == "B"
        and diagram[2][7] == "C"
        and diagram[3][7] == "C"
        and diagram[2][9] == "D"
        and diagram[3][9] == "D"
    )


def return_next_states(cost, diagram):
    """Return all possible next states for the amphipod."""
    states = []

    amphipods = []
    for y in range(len(diagram)):
        for x in range(len(diagram[0])):
            if diagram[y][x] in "ABCD":
                amphipods.append([diagram[y][x], [x, y]])

    for amphipod, (x, y) in amphipods:
        positions = reachable_positions(x, y, diagram)

        for xn, yn in positions:
            if can_move_to(amphipod, x, y, xn, yn, diagram):
                new_diagram = list(map(list, diagram))

                new_diagram[y][x] = "."
                new_diagram[yn][xn] = amphipod
                new_cost = cost + positions[(xn, yn)] * move_cost(amphipod)

                states.append((new_cost, tuple(map(tuple, new_diagram))))

    return states


def pprint(diagram):
    for l in diagram:
        print("".join(l))
    print()


states = [(0, tuple(map(tuple, diagram)))]

explored = {}

while len(states) != 0:
    cost, diagram = heappop(states)

    if diagram in explored:
        continue

    explored[diagram] = cost

    if is_correct(diagram):
        success(cost)

    for new_cost, new_diagram in return_next_states(cost, diagram):

        heappush(states, (new_cost, new_diagram))
