import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = list(map(int, get_input(whole=True).split(",")))

state = input

for i in range(80):
    new_state = []

    new_fish = 0
    for s in state:
        if s != 0:
            new_state.append(s - 1)
        else:
            new_state.append(6)
            new_fish += 1

    new_state += [8] * new_fish
    state = new_state

success(len(state))
