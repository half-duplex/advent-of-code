#!/usr/bin/env python3

search = "shiny gold"

rules = {}
with open("input.txt", "r") as f:
    for rule in f.read().strip().split("\n"):
        outer, inner_raw = rule.split(" contain ", 1)
        outer = outer[:-5]  # strip " bags"
        inner = {}
        for inner_option in inner_raw.split(","):
            inner_option = inner_option.strip(" .")
            inner_count, inner_color = inner_option.split(" ", 1)

            if inner_count == "no":
                inner_count = 0
            else:
                inner_count = int(inner_count)

            for bag in [" bag", " bags"]:
                if inner_color.endswith(bag):
                    inner_color = inner_color[: -len(bag)]
            inner[inner_color] = inner_count
        rules[outer] = inner

search_colors = {search}

last_count = 0
new_search_colors = set(search_colors)
while True:
    for outer, inner in rules.items():
        for color in search_colors:
            if color in inner:
                new_search_colors.add(outer)
    if len(new_search_colors) == last_count:
        new_search_colors.remove(search)
        print("Part 1:", len(new_search_colors))
        break
    search_colors = set(new_search_colors)
    last_count = len(new_search_colors)


def count_contains(color: str) -> int:
    print("count", color)
    total = 0
    for inner, inner_count in rules[color].items():
        print("needs", inner_count, inner)
        if inner == "other":
            continue
        # +1 for this bag
        total += inner_count * (count_contains(inner) + 1)
    print("total", color, total)
    return total


print("Part 2:", count_contains(search))
