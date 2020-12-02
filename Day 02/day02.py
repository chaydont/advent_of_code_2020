def part1():
    count = 0
    with open('input.txt') as f:
        for line in f:
            if lineIsValidPart1(line):
                count += 1
    return count

def lineIsValidPart1(line):
    min_max, letter, password = line.split()
    min_max = min_max.split('-')
    min = int(min_max[0])
    max = int(min_max[1])
    letter = letter[0]
    count = 0
    for l in password:
        if l == letter:
            count += 1
    return count >= min and count <= max



def part2():
    count = 0
    with open('input.txt') as f:
        for line in f:
            if lineIsValidPart2(line):
                count += 1
    return count

def lineIsValidPart2(line):
    positions, letter, password = line.split()
    positions = positions.split('-')
    pos1 = int(positions[0]) - 1
    pos2 = int(positions[1]) - 1
    letter = letter[0]
    return (password[pos1] == letter) ^ (password[pos2] == letter)

print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())