#!/usr/bin/env python3

import re

required_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
}

passports = []

with open("input.txt", "r") as f:
    data = {}
    for line in f:
        if len(line.strip()) == 0:
            passports.append(data)
            data = {}
            continue
        params = line.strip().split(" ")
        for param in params:
            key, value = param.split(":")
            data[key] = value
    passports.append(data)

valid_passports_1 = 0
valid_passports_2 = 0
for passport in passports:
    if not set(passport.keys()).issuperset(set(required_fields)):
        continue
    valid_passports_1 += 1

    valid = True
    print()
    for param, value in passport.items():
        print("test", param, repr(value))
        if param == "byr":
            ival = int(value)
            if ival < 1920 or ival > 2002:
                valid = False
        elif param == "iyr":
            ival = int(value)
            if ival < 2010 or ival > 2020:
                valid = False
        elif param == "eyr":
            ival = int(value)
            if ival < 2020 or ival > 2030:
                valid = False
        elif param == "hgt":
            if len(value) < 3:
                valid = False
                break
            ival = int(value[:-2])
            if value.endswith("cm") and (ival < 150 or ival > 193):
                valid = False
            elif value.endswith("in") and (ival < 59 or ival > 76):
                valid = False
        elif param == "hcl":
            if not re.match(r"#[0-9a-z]{6}", value):
                valid = False
        elif param == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
        elif param == "pid":
            if len(value) != 9 or not value.isnumeric():
                valid = False

        if not valid:
            break

    if valid:
        valid_passports_2 += 1

print("Valid part 1:", valid_passports_1)
print("Valid part 2:", valid_passports_2)
