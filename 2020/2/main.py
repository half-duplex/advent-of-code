#!/usr/bin/env python3

inputs = []
with open("input.txt", "r") as f:
    for line in f:
        if len(line.strip()) == 0:
            continue
        parts = line.split(" ")
        letter_range = parts[0].split("-")
        range_low = int(letter_range[0])
        range_high = int(letter_range[1])
        letter = parts[1].rstrip(":")
        inputs.append([range_low, range_high, letter, parts[2]])


def validate_password_1(letter_min: int, letter_max: int, letter: str, password: str):
    contents = {}
    for char in password:
        contents[char] = contents.get(char, 0) + 1
    if contents.get(letter, 0) >= letter_min and contents.get(letter, 0) <= letter_max:
        return True
    return False


def validate_password_2(pos_1: int, pos_2: int, letter: str, password: str):
    pos_1 -= 1
    pos_2 -= 1
    if password[pos_1] == letter and password[pos_2] == letter:
        return False
    if password[pos_1] == letter or password[pos_2] == letter:
        return True
    return False


valid1 = 0
valid2 = 0
for candidate in inputs:
    if validate_password_1(*candidate):
        valid1 += 1
    if validate_password_2(*candidate):
        valid2 += 1

print("Part 1 valid:", valid1)
print("Part 2 valid:", valid2)
