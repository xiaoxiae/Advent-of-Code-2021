import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

total = 0

for line in input:
    pre, post = line.split(" | ")
    pre = pre.split()
    post = post.split()

    for part in post:
        if len(part) in (2, 4, 3, 7):
            total += 1

success(total)
