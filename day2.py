def policy_one(password, min, max):
    occurrences = [c for c in password].count(character)
    return int(min) <= occurrences <= int(max)


def policy_two(password, character, first, second):
    return password[int(first) - 1] == character and password[int(second) - 1] != character or password[int(second) - 1] == character and password[int(first) - 1] != character


data = []
with open("resources/day2.data") as file:
    for line in file:
        data.append(line)

first_valid = 0
second_valid = 0
for i in range(len(data)):
    policy_range, character_with_dots, password = data[i].split(' ')
    first, second = policy_range.split('-')
    character = character_with_dots[:-1]
    if policy_one(password, first, second):
        first_valid += 1

    if policy_two(password, character, first, second):
        second_valid += 1
print('First part: {} passwords are valid'.format(first_valid))
print('Second part: {} passwords are valid'.format(second_valid))