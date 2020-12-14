with open('input.txt') as stream:
    beginning = int(stream.readline())
    busList = [(i, int(bus)) for i, bus in enumerate(stream.readline().split(',')) \
        if bus != 'x']

def part1():
    fastest = 10000000
    score = 0
    for i, bus in busList:
        wait = bus - (beginning % bus)
        if wait < fastest:
            fastest = wait
            score = bus * wait
    return score

def part2(): # un peu triché
    timestamp = 0
    step = 1
    for i, bus in busList:
        while (timestamp + i) % bus != 0:
            timestamp += step
        step *= bus
    return timestamp

print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())