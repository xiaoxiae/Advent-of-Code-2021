import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from typing import *
from heapq import *

diagram = get_input()

room_count = 11
rooms = [[] for _ in range(room_count)]
room_sizes = [1, 1, 4, 1, 4, 1, 4, 1, 4, 1, 1]
start_end_cost = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]


# parse the input
for y, line in enumerate(diagram):
    for x, v in enumerate(line):
        if v in "ABCD":
            rooms[((x - 3) // 2 + 1) * 2].insert(0, v)


for line in [["D", "C", "B", "A"], ["D", "B", "A", "C"]]:
    for i, char in enumerate(line):
        rooms[i * 2 + 2].insert(1, char)


def empty_spaces(i, rooms):
    """Return the number of empty spaces in a room."""
    return room_sizes[i] - len(rooms[i])


def is_full(i, rooms):
    """Return True if the i-th room is full."""
    return empty_spaces(i, rooms) == 0


def is_passthrough(i, rooms):
    """Return True if the i-th room can be passed through when it's full."""
    return [False, False, True, False, True, False, True, False, True, False, False][i]


def is_room(i):
    return i % 2 == 0 and i != 0 and i != room_count - 1


def is_hallway(i):
    return not is_room(i)


def correct_room_amphipod(i):
    """Return the amphipod that should be in the specified room."""
    return {2: "A", 4: "B", 6: "C", 8: "D"}[i]


def possible_moves(amphipod, i, rooms) -> Dict[int, int]:
    """Return rooms where the amphipod from the position i could move to and the price
    of this move."""
    moves = []

    # attempt to move to the left and to the right from the i-th room
    for dx in (-1, 1):
        j = i + dx
        # while in range
        while j >= 0 and j < len(rooms):
            if is_full(j, rooms):
                # don't move past the filled passthrough rooms
                if not is_passthrough(j, rooms):
                    break
            else:
                # only move to the correct room from a hallway, if it contains only valid amphipods
                if (
                    is_hallway(i)
                    and is_room(j)
                    and correct_room_amphipod(j) == amphipod
                    and contains_only_valid_amphipods(j, rooms)
                ):
                    moves.append(j)

                # can move from a room to a hallway
                if is_room(i) and is_hallway(j):
                    moves.append(j)

            j += dx

    return moves


def move_cost(amphipod) -> int:
    """Return the cost of moving an amphipod."""
    return {"A": 1, "B": 10, "C": 100, "D": 1000}[amphipod]


def is_correct(rooms) -> bool:
    """Return True if the room layout is correct."""
    for i, a in enumerate("ABCD"):
        c = i * 2 + 2

        if not is_full(c, rooms) or not contains_only_valid_amphipods(c, rooms):
            return False

    return True


def contains_only_valid_amphipods(i, rooms) -> bool:
    """Return True if there are only valid creatures in the room."""
    return all([v == correct_room_amphipod(i) for v in rooms[i]])


def return_next_states(cost, rooms):
    """Return all possible next states for the amphipod."""
    states = []

    for i in range(len(rooms)):
        if len(rooms[i]) != 0:
            amphipod = rooms[i][-1]
            for j in possible_moves(amphipod, i, rooms):
                cost_delta = (start_end_cost[i] + empty_spaces(i, rooms)) * move_cost(
                    amphipod
                )

                for k in range(min(i, j) + 1, max(i, j)):
                    cost_delta += move_cost(amphipod)

                cost_delta += (start_end_cost[j] + empty_spaces(j, rooms)) * move_cost(
                    amphipod
                )

                new_rooms = list(map(list, rooms))

                new_rooms[j].append(new_rooms[i].pop())

                states.append((cost + cost_delta, tuple(map(tuple, new_rooms))))

    return states


states = [(0, tuple(map(tuple, rooms)))]

explored = {}

while len(states) != 0:
    cost, rooms = heappop(states)

    if rooms in explored:
        continue

    explored[rooms] = cost

    if is_correct(rooms):
        success(cost)

    for new_cost, new_rooms in return_next_states(cost, rooms):
        heappush(states, (new_cost, new_rooms))
