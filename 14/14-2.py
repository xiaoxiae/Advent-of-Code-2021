import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input(whole=True)

template, rules_str = input.split("\n\n")
rules = {}
for rule in rules_str.splitlines():
    a, b = rule.split(" -> ")
    rules[a] = b

rule_counts = {}
for i in range(len(template) - 1):
    part = template[i : i + 2]
    if part not in rule_counts:
        rule_counts[part] = 1
    else:
        rule_counts[part] += 1

for i in range(40):
    new_rule_counts = {}

    for rule in rule_counts:
        # two new rules
        a = rule[0] + rules[rule]
        b = rules[rule] + rule[1]

        if a not in new_rule_counts:
            new_rule_counts[a] = rule_counts[rule]
        else:
            new_rule_counts[a] += rule_counts[rule]

        if b not in new_rule_counts:
            new_rule_counts[b] = rule_counts[rule]
        else:
            new_rule_counts[b] += rule_counts[rule]

    rule_counts = new_rule_counts

quantity = {}
for rule in rule_counts:
    a, b = rule[0], rule[1]
    c = rule_counts[rule]

    if a not in quantity:
        quantity[a] = c
    else:
        quantity[a] += c

    if b not in quantity:
        quantity[b] = c
    else:
        quantity[b] += c

# all elements except the first and last are counted twice
quantity[template[0]] += 1
quantity[template[-1]] += 1

for k in quantity:
    quantity[k] //= 2

min_val = float("inf")
max_val = 0

for c in quantity:
    if quantity[c] < min_val:
        min_val = quantity[c]
    if quantity[c] > max_val:
        max_val = quantity[c]

print(max_val - min_val)
