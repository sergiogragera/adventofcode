def is_valid(preamble, number):
    for i in range(len(preamble) - 1):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False


def find_contiguous_range(data, number):
    for i in range(len(data)):
        accum = 0
        j = i
        while j < len(data) and accum < number:
            accum += data[j]
            j += 1
        if accum == number:
            return (min(data[i:j]), max(data[i:j]))
    return (None, None)


preamble = 25
with open('resources/day9.data') as file:
    lines = []
    for line in file:
        lines.append(int(line[:-1]))

    i = 0
    found = False
    while i < len(lines) - preamble and is_valid(lines[i:i + preamble], lines[i + preamble]):
        i += 1
    invalid_number = lines[i + preamble]
    print('Fist part: the first number that dows not have this property is {}'.format(invalid_number))
    min_num, max_num = find_contiguous_range(lines, invalid_number)
    print('Second part: encryption weaknes is {} + {} = {}'.format(min_num, max_num, min_num + max_num))
