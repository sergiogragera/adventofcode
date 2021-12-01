# https://adventofcode.com/2021/day/1

def is_increasing(a, b):
    return int(a) <= int(b)


with open('2021/resources/day1.1.txt', 'r') as file:
    measurements = file.readlines()
    increases = sum([is_increasing(measurements[i], measurements[i + 1])
                    for i in range(len(measurements) - 1)])
    print('There are {} measurements that are larger than previous measurement'.format(increases))
