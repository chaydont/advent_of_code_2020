import os

def part1():
    memory = []
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        for line in f:
            current = int(line)
            for value in memory:
                if current + value == 2020:
                    return current * value
            memory.append(current)

def part2():
    memory = []
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        for line in f:
            v1 = int(line)
            for v2 in memory:
                if v1 + v2 < 2020:
                    for v3 in memory:
                        if v2 != v3 and v1 + v2 + v3 == 2020:
                            return v1 * v2 * v3
            memory.append(v1)


if __name__ == "__main__":
    print("Part 1 : %d" % part1())
    print("Part 2 : %d" % part2())