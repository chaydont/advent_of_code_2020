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
        memory[last], last = index, index - memory[last] if last in memory.keys() else 0
        index += 1
    return last

def part1():
    return algo(2020)

def part2():
    return algo(30000000)

print("\rPart 1 : %s" % part1())
print("\rPart 2 : %s" % part2())