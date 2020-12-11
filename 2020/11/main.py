#!/usr/bin/env python3

with open("input.txt", "r") as f:
    original_board = f.read().strip().split("\n")


def print_board(board):
    print()
    for row in board:
        print("".join(row))
    print()


def search_around(board, row, column, search):
    count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            if row + x < 0 or row + x >= len(board):
                continue
            if column + y < 0 or column + y >= len(board[0]):
                continue
            if board[row + x][column + y] == search:
                count += 1
    return count


board = list(original_board)
while True:
    next_board = [list(x) for x in board]
    changed = False
    for idxr, row in enumerate(board):
        for idxc, cell in enumerate(row):
            # print("eval", cell, "at", idxr, idxc)
            if cell == ".":
                next_board[idxr][idxc] = "."
            elif cell == "L":
                if search_around(board, idxr, idxc, "#") == 0:
                    next_board[idxr][idxc] = "#"
                    changed = True
            elif cell == "#":
                if search_around(board, idxr, idxc, "#") >= 4:
                    next_board[idxr][idxc] = "L"
                    changed = True
            else:
                print("Invalid cell contents", cell, "at", idxr, idxc)
                exit()
    if not changed:
        break
    board = next_board

count = 0
for row in board:
    for cell in row:
        if cell == "#":
            count += 1
print("Part 1:", count)


def search_vector(board, row, column, search):
    count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            c_row = row + x
            c_col = column + y
            while (
                c_row >= 0
                and c_row < len(board)
                and c_col >= 0
                and c_col < len(board[0])
            ):
                if board[c_row][c_col] == search:
                    count += 1
                elif board[c_row][c_col] == ".":
                    c_row += x
                    c_col += y
                    continue
                break
    # print("counted", count, "of", search, "around", row, column)
    return count


board = list(original_board)
while True:
    next_board = [list(x) for x in board]
    changed = False
    for idxr, row in enumerate(board):
        for idxc, cell in enumerate(row):
            # print("eval", cell, "at", idxr, idxc)
            if cell == ".":
                next_board[idxr][idxc] = "."
            elif cell == "L":
                if search_vector(board, idxr, idxc, "#") == 0:
                    next_board[idxr][idxc] = "#"
                    changed = True
            elif cell == "#":
                if search_vector(board, idxr, idxc, "#") >= 5:
                    next_board[idxr][idxc] = "L"
                    changed = True
            else:
                print("Invalid cell contents", cell, "at", idxr, idxc)
                exit()
    if not changed:
        print("No change")
        break
    board = next_board

count = 0
for row in board:
    for cell in row:
        if cell == "#":
            count += 1

print("Part 2:", count)
