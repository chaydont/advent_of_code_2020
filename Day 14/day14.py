import re
import itertools

def parse(line):
    pattern = re.compile(r"^(mem)\[([\d]+)\] = ([\d]+)$")
    if line.startswith('mask'):
        return tuple(line.split(' = '))
    if line.startswith('mem'):
        a = pattern.match(line)
        key = '{0:036b}'.format(int(a.group(2)))
        n = '{0:036b}'.format(int(a.group(3)))
        return (a.group(1), key, n)

program = [parse(line) for line in open('input.txt').readlines()]

def part1():
    mem = {}
    for line in program:
        if line[0] == 'mask':
            mask = line[1].strip()
        elif line[0] == 'mem':
            mem[int(line[1], 2)] = applyMask(line[2], mask, 'X')
    total = 0
    for value in mem.values():
        total += int(value, 2)
    return total

def part2():
    mem = {}
    for line in program:
        if line[0] == 'mask':
            mask = line[1].strip()
        elif line[0] == 'mem':
            value = applyMask(line[1], mask, '0')
            min_value = []
            Xes = []
            for i in range(0, 36):
                if value[i] == 'X':
                    min_value.append('0')
                    Xes.append(pow(2, 35 - i))
                else:
                    min_value.append(value[i])
            min_value = ''.join(min_value)
            mem[int(min_value, 2)] = line[2]
            for i in range(1, len(Xes) + 1):
                for a in itertools.combinations(Xes, i):
                    mem[int(min_value, 2) + sum(a)] = line[2]
    total = 0
    for value in mem.values():
        total += int(value, 2)
    return total
    
def applyMask(value, mask, replaced):
    str_list = []
    for i in range(0, 36):
        if mask[i] == replaced:
            str_list.append(value[i])
        else:
            str_list.append(mask[i])
    return ''.join(str_list)
            


print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())