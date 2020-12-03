with open('input.txt') as stream:
    map = [a.strip() for a in stream.readlines()]

def part1():
    return a(1, 3)

def part2():
    return a(1, 1) * a(1, 3) * a(1, 5) * a(1, 7) * a(2, 1)

def a(slopeY, slopeX):
    length = len(map[0])
    pos = 0
    count = 0
    i = 0
    while i < len(map):
        if map[i][pos % length] == '#':
            count += 1
        pos += slopeX
        i += slopeY
    return count

print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())
