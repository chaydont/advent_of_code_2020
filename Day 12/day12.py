with open('input.txt') as stream:
    instructions = [(line[0], int(line[1:])) for line in stream.readlines()]

def moveTo(x, y, direction, length):
    if direction == 'N':   y += length
    elif direction == 'E': x += length
    elif direction == 'S': y -= length
    elif direction == 'W': x -= length
    return x, y

def turnRight(direction, n):
    for i in range(0, n):
        direction = turnRightOnce(direction)
    return direction

def turnRightOnce(direction):
    if direction == 'N':   return 'E'
    elif direction == 'E': return 'S'
    elif direction == 'S': return 'W'
    elif direction == 'W': return 'N'

def part1():
    x, y = 0, 0
    direction = 'E'
    for instruction in instructions:
        if instruction[0] in ('N', 'S', 'E', 'W'):
            x, y = moveTo(x, y, instruction[0], instruction[1])
        elif instruction[0] == 'F':
            x, y = moveTo(x, y, direction, instruction[1])
        elif instruction[0] == 'R':
            direction = turnRight(direction, int(instruction[1] / 90))
        elif instruction[0] == 'L':
            direction = turnRight(direction, 4 - int(instruction[1] / 90))
    return abs(x) + abs(y)

def rotateWayPoint(wx, wy, n):
    for i in range(0, n):
        wx, wy = wy, -wx
    return wx, wy

def part2():
    x, y = 0, 0
    wx, wy = 10, 1
    for instruction in instructions:
        if instruction[0] in ('N', 'S', 'E', 'W'):
            wx, wy = moveTo(wx, wy, instruction[0], instruction[1])
        elif instruction[0] == 'F':
            x += wx * instruction[1]
            y += wy * instruction[1]
        elif instruction[0] == 'R':
            wx, wy = rotateWayPoint(wx, wy, int(instruction[1] / 90))
        elif instruction[0] == 'L':
            wx, wy = rotateWayPoint(wx, wy,  4 - int(instruction[1] / 90))
    return abs(x) + abs(y)


print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())