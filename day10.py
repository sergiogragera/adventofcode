import regex

with open('resources/day10.data') as file:
    sequence = []
    for line in file:
        sequence.append(int(line[:-1]))
    sequence.sort()
    sequence = [0] + sequence + [(sequence[-1] + 3)]

    diffs = ''
    for i in range(1, len(sequence)):
        diffs += str(sequence[i] - sequence[i - 1])

    compile = regex.compile(r'^((1)|(3))+$')
    match = compile.match(diffs)
    ones = match.captures(2)
    threes = match.captures(3)
    print('Fist part: there are {0} differences of 1 jolt and {1} differences of 3 jolts. {0} * {1} = {2}'.format(len(ones), len(threes), len(ones) * len(threes)))

    compile = regex.compile(r'^((1{4})|(1{3})|(1{2})|1|3)+$')
    match = compile.match(diffs)
    four_ones_in_a_row = match.captures(2)
    three_ones_in_a_row = match.captures(3)
    two_ones_in_a_row = match.captures(4)
    result = pow(7, len(four_ones_in_a_row)) * pow(4, len(three_ones_in_a_row)) * pow(2, len(two_ones_in_a_row))
    print('Second part: the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device is {}'.format(result))
