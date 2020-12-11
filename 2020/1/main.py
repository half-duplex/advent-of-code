#!/usr/bin/env python3

with open("input.txt", "r") as f:
    numbers = [int(x) for x in f.read().split("\n") if len(x.strip()) > 0]

# Part 1
found = False
for idx, num in enumerate(numbers):
    for idx2, num2 in enumerate(numbers):
        if idx2 == idx:
            continue
        if num + num2 == 2020:
            print("Part 1 answer:", num * num2)
            found = True
            break
    if found:
        break

# Part 2
found = False
for idx, num in enumerate(numbers):
    for idx2, num2 in enumerate(numbers):
        if idx2 == idx:
            continue
        for idx3, num3 in enumerate(numbers):
            if idx3 == idx2 or idx3 == idx:
                continue
            if num + num2 + num3 == 2020:
                print("Part 2 answer:", num * num2 * num3)
                found = True
                break
        if found:
            break
    if found:
        break
