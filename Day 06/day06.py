with open('input.txt') as stream:
    lines = [line.strip() for line in stream]

def part1():
    return logic(lambda a, b: a.union(b))

def part2():
    return logic(lambda a, b: a.intersection(b))

def logic(func):
    count = 0
    current = None
    for line in lines:
        if current == None: # first line of group
            current = {letter for letter in line}
        elif line == "": # end of group
            count += len(current)
            current = None
        else:
            current = func(current, {letter for letter in line})
    count += len(current) # last group
    return count

print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())