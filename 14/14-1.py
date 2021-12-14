import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input(whole=True)

template, rules_str = input.split("\n\n")
rules = {}
for rule in rules_str.splitlines():
    a, b = rule.split(" -> ")
    rules[a] = b

for i in range(5):
    new_template = ""

    for j in range(len(template) - 1):
        part = template[j : j + 2]
        new_template += part[0]

        if part in rules:
            new_template += rules[part]
        else:
            print("wow")
            quit()
    new_template += template[-1]

    print(template)
    template = new_template

quantity = {}
for c in template:
    if c not in quantity:
        quantity[c] = 1
    else:
        quantity[c] += 1

min_val = float("inf")
max_val = 0

for c in quantity:
    if quantity[c] < min_val:
        min_val = quantity[c]
    if quantity[c] > max_val:
        max_val = quantity[c]

print(max_val - min_val)
