#!/usr/bin/env python3

with open("input.txt", "r") as f:
    groups_raw = f.read().split("\n\n")

yes_sum = 0
for group_raw in groups_raw:
    yeses = set(group_raw)
    if "\n" in yeses:
        yeses.remove("\n")
    yes_sum += len(yeses)
print("Part 1:", yes_sum)

yes_sum = 0
for group_raw in groups_raw:
    all_yes = set("abcdefghijklmnopqrstuvwxyz")
    for person in group_raw.strip().split("\n"):
        all_yes = all_yes.intersection(set(person))
    yes_sum += len(all_yes)
print("Part 2:", yes_sum)
