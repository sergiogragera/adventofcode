goal = 2020
data = []
with open("resources/day1.data") as file:
    for line in file:
        data.append(int(line))

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] + data[j] == goal:
            print('First part: {} and {} sum {} and if you multiply them the result is {}'.format(data[i], data[j], goal, data[i] * data[j]))

        for k in range(j + 1, len(data)):
            if data[i] + data[j] + data[k] == goal:
                print('Second part: {} and {} and {} sum {} and if you multiply them the result is {}'.format(data[i], data[j], data[k], goal, data[i] * data[j] * data[k]))
