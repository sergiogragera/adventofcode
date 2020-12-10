import regex


code_sw_fix = {
    'jmp': 'nop',
    'nop': 'jmp'
}
pattern = regex.compile(r'(acc|jmp|nop) ([\+-]\d+)')


def exec_code(lines, bug_line=-1):
    exec_lines = []
    acc = 0
    i = 0
    while i not in exec_lines and i < len(lines):
        exec_lines.append(i)
        match = pattern.match(lines[i])
        sw = {
            'acc': (int(match.group(2)), i + 1),
            'jmp': (0, i + int(match.group(2))),
            'nop': (0, i + 1)
        }
        i_acc, i = sw.get(code_sw_fix.get(match.group(1)) if bug_line == i else match.group(1), (0, i + 1))
        acc += i_acc
    return i >= len(lines), acc


with open('resources/day8.data') as file:
    lines = []
    for line in file:
        lines.append(line[:-1])
    result = exec_code(lines)
    print('Fist part: the value in the accumulator is {}'.format(result[1]))
    bug_line = -1
    while not result[0]:
        if not result[0]:
            bug_line = next(s for s, x in enumerate(lines) if (x.startswith('jmp') or x.startswith('nop')) and s > bug_line)
            result = exec_code(lines, bug_line)
    print('Second part: the value in the accumulator when fix code and no exists infinite loops is {}'.format(result[1]))
