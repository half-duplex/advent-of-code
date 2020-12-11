#!/usr/bin/env python3

from math import ceil

passes = []
with open("input.txt", "r") as f:
    for line in f:
        passes.append(line.strip())


def find_seat(passe):
    low = 0
    high = 127

    for char in passe[:7]:
        if char == "F":
            high = (high + low) // 2
        if char == "B":
            low = ceil((high + low) / 2)
    row = low

    low = 0
    high = 7
    for char in passe[7:]:
        if char == "L":
            high = (high + low) // 2
        if char == "R":
            low = ceil((high + low) / 2)
    column = low

    return row * 8 + column


assert find_seat("FBFBBFFRLR") == 357
assert find_seat("BFFFBBFRRR") == 567
assert find_seat("FFFBBBFRRR") == 119
assert find_seat("BBFFBBFRLL") == 820

max_seat_id = 0
seats = [False] * 128 * 8
for passe in passes:
    seat = find_seat(passe)
    if seat > max_seat_id:
        max_seat_id = seat
    seats[seat] = True

started = False
my_seat = None
for seat_id, filled in enumerate(seats):
    if filled and not started:
        started = True
    elif started and not filled:
        my_seat = seat_id
        break

print("Part 1:", max_seat_id)
print("Part 2:", my_seat)
