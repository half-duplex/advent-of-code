#!/usr/bin/env python3

map_data = []
map_width = 0

with open("input.txt", "r") as f:
    for line in f:
        if len(line.strip()) == 0:
            continue
        map_data.append(line.strip())
map_width = len(map_data[0])


def check_slope(slope_x, slope_y):
    trees = 0
    pos_x, pos_y = 0, 0
    while True:
        # print(pos_x, pos_y)
        if map_data[pos_y][pos_x] == "#":
            trees += 1
        pos_x = (pos_x + slope_x) % map_width
        pos_y = pos_y + slope_y
        if pos_y >= len(map_data):
            break
    return trees


slope_x, slope_y = 3, 1
trees = check_slope(slope_x, slope_y)
print("Part 1 trees:", trees)

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
product = 1
for slope_x, slope_y in slopes:
    product *= check_slope(slope_x, slope_y)
print("Part 2 trees:", product)
