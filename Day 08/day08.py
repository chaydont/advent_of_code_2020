with open('input.txt') as stream:
    code = [{'op': a.split()[0], 'value': int(a.split()[1])} for a in stream]

def exec(code):
    index = 0
    acc = 0
    visited = []
    while True:
        if index in visited:
            return {'exception': True, 'acc': acc}
        elif index >= len(code):
            return {'exception': False, 'acc': acc}
        visited.append(index)
        instr = code[index]
        index += instr['value'] if instr['op'] == 'jmp' else 1
        acc   += instr['value'] if instr['op'] == 'acc' else 0

def part1():
    return exec(code)['acc']

def part2():
    for index in range(0, len(code)):
        if code[index]['op'] in ['jmp', 'nop']:
            code[index]['op'] = 'jmp' if code[index]['op'] == 'nop' else 'nop'
            res = exec(code)
            if not res['exception']:
                return res['acc']
            code[index]['op'] = 'jmp' if code[index]['op'] == 'nop' else 'nop'
    raise Exception("No fix found")

print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())