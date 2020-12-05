import re

with open("input.txt") as stream:
    lines = [a.strip() for a in stream]

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def part1():
    return checkPassports(passportIsValid)

def part2():
    return checkPassports(passportIsFullyValid)

def checkPassports(passportChecker):
    count = 0
    passport = {}
    for line in lines:
        if line == "":
            if passportChecker(passport):
                count += 1
            passport = {}
        else:
            for field in line.split():
                key, value = field.split(':')
                if key in required_fields:
                    passport[key] = value
    if passportChecker(passport):
        count += 1
    return count

def passportIsValid(passport):
    for field in required_fields:
        if field not in passport:
            return False
    return True

def passportIsFullyValid(passport):
    for field in required_fields:
        if field not in passport:
            return False
        value = passport[field]
        if field == 'byr':
            if not dateBetween(value, 1920, 2002):
                return False
        elif field == 'iyr':
            if not dateBetween(value, 2010, 2020):
                return False
        elif field == 'eyr':
            if not dateBetween(value, 2020, 2030):
                return False
        elif field == 'hgt':
            match = re.search('^([0-9]+)(cm|in)$', value)
            if match is None:
                return False
            value, unit = match.groups()
            if (unit == 'cm' and not between(value, 150, 193)) or \
               (unit == 'in' and not between(value, 59, 76)):
                return False
        elif field == 'hcl':
            if re.search('^#[0-9a-f]{6}$', value) is None:
                return False
        elif field == 'ecl':
            if re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', value) is None:
                return False
        elif field == 'pid':
            if re.search('^[0-9]{9}$', value) is None:
                return False
    return True


def dateBetween(value, min, max):
    match = re.search('^[0-9]{4}$', value)
    return match is not None and between(match.group(), min, max)

def between(value, min, max):
    return int(value) >= min and int(value) <= max

print("Part 1 : %s" % part1())
print("Part 2 : %s" % part2())
