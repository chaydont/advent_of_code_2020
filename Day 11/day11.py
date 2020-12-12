import copy

plane = [list(line.strip()) for line in open('input.txt').readlines()]

def step(func, plane, n):
    tmp = copy.deepcopy(plane)
    for y, row in enumerate(plane):
        for x, seat in enumerate(row):
            if seat == 'L' and func(plane, y, x) == 0:
                tmp[y][x] = '#'
    plane = copy.deepcopy(tmp)
    for y, row in enumerate(plane):
        for x, seat in enumerate(row):
            if seat == '#' and func(plane, y, x) >= n:
                tmp[y][x] = 'L'
    return copy.deepcopy(tmp)
            
def countOccupied(plane):
    count = 0
    for row in plane:
        for seat in row:
            if seat == '#':
                count += 1
    return count

def countAdjacentSeat(plane, y, x):
    count = 0
    for i, j in getDirections():
        if x + i >= 0 and x + i < len(plane[0]) \
        and y + j >= 0 and y + j< len(plane) and plane[y + j][x + i] == '#':
            count += 1
    return count

def countAdjacentSeat2(plane, y, x):
    count = 0
    for direction in getDirections():
        if seeSomeone(plane, y, x, direction):
            count += 1
    return count

def seeSomeone(plane, y, x, direction):
    i, j = direction
    k = 1
    while x + i * k >= 0 and x + i * k < len(plane[0]) \
      and y + j * k >= 0 and y + j * k < len(plane):
        current = plane[y + j * k][x + i * k]
        if current != '.':
            return current == '#'
        k += 1

def getDirections():
    return [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

def program(func, n):
    occupied = 0
    last = -1
    currentPlane = copy.deepcopy(plane)
    while True:
        occupied = countOccupied(currentPlane)
        currentPlane = step(func, currentPlane, n)
        if occupied == countOccupied(currentPlane):
            return occupied

def part1():
    return program(countAdjacentSeat, 4)

def part2():
    return program(countAdjacentSeat2, 5)
        
print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())