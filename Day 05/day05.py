with open('input.txt') as stream:
    inputs = [line.strip() for line in stream]

def part1():
    max = 0
    for boardingPass in inputs:
        seatNumber = getSeatNumber(boardingPass)
        max = seatNumber if seatNumber > max else max
    return max

def part2():
    passengers = []
    for boardingPass in inputs:
        passengers.append(getSeatNumber(boardingPass))
    passengers.sort()
    last = passengers[0] - 1
    for p in passengers:
        if p - 1 != last:
            return p - 1
        last = p


def getSeatNumber(bp):
    return getBinaryValue(bp[0:7], 'B') * 8 + getBinaryValue(bp[7:11], 'R')

def getBinaryValue(str, ones):
    value = 0
    for i in range(0, len(str)):
        if str[len(str) - i - 1] == ones:
            value += pow(2, i)
    return value

print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())