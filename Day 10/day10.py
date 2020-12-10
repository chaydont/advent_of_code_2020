from functools import lru_cache

with open('input.txt') as stream:
    adapters = [int(a) for a in stream]
    adapters.sort()

def part1():
    current, ones, trees = 0, 0, 1
    for adapter in adapters:
        if adapter - current == 1: ones += 1
        if adapter - current == 3: trees += 1
        current = adapter
    return ones * trees

@lru_cache(maxsize=None)
def countPossibilitesFrom(i):
    if i == len(adapters) - 1:
        return 1
    value = 0
    for j in range(1, 4):
        if i + j < len(adapters) and adapters[i + j] - adapters[i] <= 3:
            value += countPossibilitesFrom(i + j)
    return value

def part2():
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    return countPossibilitesFrom(0)

print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())