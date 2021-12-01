# https://adventofcode.com/2021/day/1#part1

def is_increasing(a, b):
    return int(a) < int(b)


def get_increasements(measurements):
    sum([is_increasing(measurements[i], measurements[i + 1])
         for i in range(len(measurements) - 1)])


with open('2021/resources/day1.1.txt', 'r') as file:
    measurements = file.readlines()
    print('There are {} measurements that are larger than previous measurement'.format(
        get_increasements(measurements)))
