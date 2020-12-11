#!/usr/bin/env python3


class LoopingException(Exception):
    pass


instructions = []
with open("input.txt", "r") as f:
    for line in f:
        opcode, value = line.strip().split(" ")
        value = int(value)
        instructions.append((opcode, value))


def execute(instructions, exec_cap=None, raise_repeats=False):
    eax = 0
    acc = 0
    executed = [0] * len(instructions)
    while True:
        # Ran to completion
        if eax >= len(instructions):
            return acc

        # Kill loops
        if exec_cap is not None and executed[eax] >= exec_cap:
            if raise_repeats:
                raise LoopingException()
            return acc
        executed[eax] += 1

        opcode, value = instructions[eax]
        # print("acc", acc, "ct", executed[eax], "eax", eax, "opcode", opcode, "val", value)
        if opcode == "acc":
            acc += value
        elif opcode == "jmp":
            eax += value
            continue
        elif opcode == "nop":
            pass
        else:
            print("Unknown opcode at {}: {} {}".format(eax, opcode, value))
        eax += 1


# assert execute(instructions, 1) == 1684
print("Part 1:", execute(instructions, 1))

for i in range(len(instructions)):
    instr_copy = list(instructions)
    if instructions[i][0] == "jmp":
        instr_copy[i] = ("nop", instr_copy[i][1])
    elif instructions[i][0] == "nop":
        instr_copy[i] = ("jmp", instr_copy[i][1])
    else:
        continue
    try:
        print("Part 2:", execute(instr_copy, 1, True))
    except LoopingException:
        pass
