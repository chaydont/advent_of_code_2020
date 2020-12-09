from queue import Queue

PREAMBLE_LENGTH = 25
with open('input.txt') as stream:
    lines = [int(a) for a in stream]

def hasSum(preamble, current):
    for i in range(0, len(preamble)):
        for j in range(i, len(preamble)):
            if (preamble[i] + preamble[j] == current):
                return True
    return False

def checkValid(n):
    preamble = lines[0:n]
    for i in range(n, len(lines)):
        if not hasSum(preamble, lines[i]):
            return lines[i]
        preamble.pop(0)
        preamble.append(lines[i])


def part1():
    return checkValid(PREAMBLE_LENGTH)

def part2():
    goal = part1()
    index = 1
    current = [lines[0]]
    while True:
        if sum(current) < goal:
            current.append(lines[index])
            index += 1
        elif sum(current) == goal:
            return min(current) + max(current)
        elif sum(current) > goal:
            current.pop(0)



print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())