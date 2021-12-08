import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

total = 0

digits = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]

total = 0
for line in input:
    pre, post = line.split(" | ")
    pre = sorted(pre.split(), key=lambda x: len(x))
    post = post.split()

    mapping = {}

    cf = list(pre[0])
    cfa = list(pre[1])

    print(pre)

    # a
    for a in cfa:
        if a not in cf:
            mapping['a'] = a

    # c f
    for part in pre:
        if len(part) != 6:
            continue

        c, f = cf

        if c in part and f not in part:
            mapping['f'] = c
            mapping['c'] = f
        elif c not in part and f in part:
            mapping['f'] = f
            mapping['c'] = c

    for part in pre:
        if len(part) != 5:
            continue

        if mapping['c'] in part and mapping['f'] in part and mapping['a'] in part:
            dg = [p for p in part if p not in cfa]

    # d g       in 4
    if dg[0] in pre[2]:
        mapping['d'] = dg[0]
        mapping['g'] = dg[1]
    else:
        mapping['d'] = dg[1]
        mapping['g'] = dg[0]

    # b
    for p in pre[2]:
        if p not in mapping.values():
            mapping['b'] = p

    # e
    for p in pre[-1]:
        if p not in mapping.values():
            mapping['e'] = p


    inverse_mapping = {}
    for p in mapping:
        inverse_mapping[mapping[p]] = p

    number = 0
    for p in post:
        p_mapped = [inverse_mapping[c] for c in p]

        number = number * 10 + digits.index("".join(sorted(p_mapped)))

    total += number


success(total)
