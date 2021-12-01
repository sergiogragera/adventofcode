import re


def is_valid(credentials):
    regex = {
        'byr': r'^(19[2-9][0-9]|200[0-2])$',
        'iyr': r'^(201[0-9]|2020)$',
        'eyr': r'^(202[0-9]|2030)$',
        'hgt': r'^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$',
        'hcl': r'^#[0-9a-f]{6}$',
        'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
        'pid': r'^\d{9}$'
    }
    if regex.keys() <= credentials.keys():
        for key in credentials:
            if key != 'cid':
                comp = re.compile(regex[key])
                if not comp.match(credentials[key]):
                    return False
        return True
    return False


def part2(data):
    valid_credentials = 0
    credentials = {}
    for line in file:
        line_withou_break = line.replace('\n', '')
        if len(line_withou_break) > 0:
            pairs = line_withou_break.split(' ')
            for pair in pairs:
                key, value = pair.split(':')
                credentials[key] = value
        else:
            valid_credentials += 1 if is_valid(credentials) else 0
            credentials = {}
    return valid_credentials


with open('resources/day4.data') as file:
    print('Second part: there are {} passports valid'.format(part2(file)))