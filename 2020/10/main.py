#!/usr/bin/env python3

with open("input.txt", "r") as f:
    data = sorted([int(x) for x in f.read().strip().split("\n")])
data = list(data) + [data[-1] + 3]

last = 0
diffs = {1: 0, 2: 0, 3: 0}
for x in data:
    diffs[x - last] += 1
    last = x
print("Part 1:", diffs[1] * diffs[3])

pathcount_cache = {}


def remaining_options(data: list, last: int, current_idx: int) -> int:
    if pathcount_cache.get((last, current_idx)) is not None:
        return pathcount_cache[(last, current_idx)]
    if current_idx == len(data) - 1:
        # print("yep")
        return 1
    # print("eval last", last, "ci", current_idx, "dci", data[current_idx], "dci1", data[current_idx+1])
    opts = remaining_options(data, data[current_idx], current_idx + 1)
    if data[current_idx + 1] - last <= 3:
        opts += remaining_options(data, last, current_idx + 1)
    pathcount_cache[(last, current_idx)] = opts
    return opts


print("Part 2:", remaining_options(data, 0, 0))
