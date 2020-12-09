import regex


def contains_shiny_gold(bags, name):
    if 'shiny gold' in bags[name]:
        return True
    elif len(bags[name]) > 0:
        for contained_name in list(set(bags[name])):
            if contains_shiny_gold(bags, contained_name):
                return True
    return False


def bags_inside_shiny_gold(bags, name='shiny gold'):
    count = 0
    if len(bags[name]) > 0:
        for b in bags[name]:
            count += bags_inside_shiny_gold(bags, b)
    return len(bags[name]) + count


with open('resources/day7.data') as file:
    count = 0
    bags = {}
    pattern = regex.compile(r'^(.+ .+) bags contain (no other bags|(,? ?(\d+) ([a-z]+ [a-z]+) bags?)+)\.$')
    for line in file:
        match = pattern.match(line[:-1])
        bags[match.group(1)] = []
        for i, e in enumerate(match.captures(4)):
            for j in range(int(match.captures(4)[i])):
                bags[match.group(1)].append(match.captures(5)[i])
    for b in bags.keys():
        if contains_shiny_gold(bags, b):
            count += 1
    print('Fist part: {} bag colors can contain at least one shiny gold bag'.format(count))
    print('Second part: shiny gold contains {} bags'.format(bags_inside_shiny_gold(bags)))
