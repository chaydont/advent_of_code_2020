import re
from functools import lru_cache

rules = {}

LINE_PATTERN = re.compile("^([a-z ]+) bags contain ([0-9a-z ,]+).$")
BAGS_PATTERN = re.compile("^([0-9]+) ([a-z ]+) bag")

def parseLine(line):
    match = LINE_PATTERN.match(line)
    if match != None and match.groups() != None:
        groups = match.groups()
        rules[groups[0]] = parseBags(groups[1])

def parseBags(bags):
    ret = []
    for bag in bags.split(', '):
        match = BAGS_PATTERN.match(bag)
        if match != None and match.groups() != None:
            groups = match.groups()
            ret.append({'number': int(groups[0]), 'color': groups[1]})
    return ret

with open('input.txt') as stream:
    for line in stream:
        parseLine(line)

@lru_cache(maxsize=None)
def canContainGoldy(currentColor):
    for color in rules[currentColor]:
        if color['color'] == 'shiny gold' or canContainGoldy(color['color']):
            return True
    return False


def part1():
    count = 0
    for color in rules.keys():
        if canContainGoldy(color):
            count +=1
    return count


def countBagsInside(color):
    total = 0
    for color in rules[color]:
        total += color['number'] * (countBagsInside(color['color']) + 1)
    return total

def part2():
    return countBagsInside('shiny gold')

print("Part 1 : %d" % part1())
print("Part 2 : %d" % part2())