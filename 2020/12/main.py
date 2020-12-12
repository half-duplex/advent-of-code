#!/usr/bin/env python3

right = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N",
}
left = {v: k for k, v in right.items()}

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")

instructions = []
for item in data:
    instructions.append((item[0], int(item[1:])))

cur_x = 0
cur_y = 0
direction = "E"
for op, value in instructions:
    if op == "R":
        for i in range(0, value, 90):
            direction = right[direction]
    elif op == "L":
        for i in range(0, value, 90):
            direction = left[direction]
    elif op == "F":
        op = direction

    if op == "N":
        cur_y += value
    elif op == "S":
        cur_y -= value
    elif op == "E":
        cur_x += value
    elif op == "W":
        cur_x -= value

print("Part 1:", abs(cur_x) + abs(cur_y))

ship_x = 0
ship_y = 0
wp_x = 10
wp_y = 1
direction = "E"
for op, value in instructions:
    if op == "N":
        wp_y += value
    elif op == "S":
        wp_y -= value
    elif op == "E":
        wp_x += value
    elif op == "W":
        wp_x -= value
    elif op == "L":
        for i in range(0, value, 90):
            wp_x, wp_y = -wp_y, wp_x
    elif op == "R":
        for i in range(0, value, 90):
            wp_x, wp_y = wp_y, -wp_x
    elif op == "F":
        ship_x += wp_x * value
        ship_y += wp_y * value

print("Part 2:", abs(ship_x) + abs(ship_y))
