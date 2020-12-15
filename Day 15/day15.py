start = [int(a) for a in open('input.txt').readline().split(',')]

def algo(n):
    memory = {}
    index = len(start) - 1
    last = start[-1]
    for i in range(0, len(start) - 1):
        memory[start[i]] = i
    while index < n - 1:
        if index % (n // 100) == 0:
            print("\r%d %%" % (100 * index / n), end = '')
        current = last
        if current in memory.keys():
            current = index - memory[current]
        else:
            current = 0
        memory[last] = index
        last = current
        index += 1
    return last

def part1():
    return algo(2020)

def part2():
    return algo(30000000)

print("\rPart 1 : %s" % part1())
print("\rPart 2 : %s" % part2())