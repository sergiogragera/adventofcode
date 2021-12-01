# https://adventofcode.com/2021/day/1#part1

def is_increasing(a, b):
    return a < b


def count_increasements(measurements):
    return sum([is_increasing(measurements[i], measurements[i + 1])
                for i in range(len(measurements) - 1)])


with open('2021/resources/day1.1.txt', 'r') as file:
    measurements = list(map(int, file.readlines()))
    print('Part 1: there are {} measurements that are larger than previous measurement'.format(
        count_increasements(measurements)))

# https://adventofcode.com/2021/day/1#part2


def reduce_noise(measurements):
    return [sum(measurements[i:i + 3]) for i in range(len(measurements) - 2)]


with open('2021/resources/day1.2.txt', 'r') as file:
    measurements = reduce_noise(list(map(int, file.readlines())))
    print('Part 2: there are {} measurements that are larger than previous measurement'.format(
        count_increasements(measurements)))
