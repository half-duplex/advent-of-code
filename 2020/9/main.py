#!/usr/bin/env python3

preamble = 25
with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().strip().split("\n")]


def is_sum(candidates: list, target: int):
    for idx, i in enumerate(candidates):
        for j in candidates[idx:]:
            if i + j == target:
                return True
    return False


part1_answer = None
for idx, num in enumerate(data[preamble:]):
    idx += preamble
    if not is_sum(data[idx - preamble : idx], num):
        part1_answer = num
        print("Part 1:", num)
        break

for idx, num in enumerate(data):
    total = num
    for idx2, num2 in enumerate(data[idx + 1 :]):
        idx2 += idx + 1
        total += num2
        if total > part1_answer:
            break
        elif total == part1_answer:
            print("Part 2:", min(data[idx : idx2 + 1]) + max(data[idx : idx2 + 1]))
            exit()
