import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = list(map(int, get_input(whole=True).split(",")))

state = input

state_counts = {i:0 for i in range(9)}
for s in state:
    state_counts[s] += 1

for i in range(256):
    new_fish = state_counts[0]

    for i in range(0, 8):
        state_counts[i] = state_counts[i + 1]
    state_counts[8] = new_fish
    state_counts[6] += new_fish

total = 0
for s in state_counts:
    total += state_counts[s]

success(total)
