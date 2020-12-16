import re

fieldList = {}
ticketList = []
validTicketList = []
myTicket = []

with open('input.txt') as stream:
    line = stream.readline()
    pattern = re.compile(r"([a-z ]+): ([\d]+)-([\d]+) or ([\d]+)-([\d]+)")
    while line != "":
        match = pattern.match(line)
        fieldList[match.group(1)] = ( \
            range(int(match.group(2)), int(match.group(3)) + 1), \
            range(int(match.group(4)), int(match.group(5)) + 1)  \
        )
        line = stream.readline().strip()

    stream.readline()
    myTicket = [int(a) for a in stream.readline().strip().split(',')]
    stream.readline()
    stream.readline()
    
    for line in stream:
        ticketList.append([int(a) for a in line.split(',')])

def part1():
    total = 0
    toRemove = []
    for i, ticket in enumerate(ticketList):
        valideTicket = True
        for value in ticket:
            valid = False
            for r in fieldList.values():
                if value in r[0] or value in r[1]:
                    valid = True
            if not valid:
                total += value
                valideTicket = False
        if not valideTicket:
            toRemove.append(i)
    global validTicketList
    validTicketList = [ticket for i, ticket in enumerate(ticketList) if i not in toRemove]
    return total

def part2():
    total = 1
    canBeThatField = {}
    found = {}
    for field in fieldList:
        canBeThatField[field] = []
        for i in range(0, len(myTicket)):
            canBeThere = True
            for ticket in validTicketList:
                if ticket[i] not in fieldList[field][0] \
                and ticket[i] not in fieldList[field][1]:
                    canBeThere = False
            if canBeThere:
                canBeThatField[field].append(i)

    while len(found) < len(myTicket):
        for field in canBeThatField:
            canBeThatField[field] = [a for a in canBeThatField[field] if a not in found.values()]
            if len(canBeThatField[field]) == 1:
                found[field] = canBeThatField[field][0]
                if field.startswith('departure'):
                    total *= myTicket[canBeThatField[field][0]]
    return total
        
print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())