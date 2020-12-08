def is_tree(i, line, right, down):
    if i > 0 and i % down == 0:
        position = (int(i / down) * right)
        return True if line[position % (len(line) - 1)] == '#' else False
    return False


tree_11 = 0
tree_31 = 0
tree_51 = 0
tree_71 = 0
tree_12 = 0
with open("resources/day3.data") as file:
    for i, line in enumerate(file):
        tree_11 += 1 if is_tree(i, line, 1, 1) else 0
        tree_31 += 1 if is_tree(i, line, 3, 1) else 0
        tree_51 += 1 if is_tree(i, line, 5, 1) else 0
        tree_71 += 1 if is_tree(i, line, 7, 1) else 0
        tree_12 += 1 if is_tree(i, line, 1, 2) else 0
print('First part: {} trees'.format(tree_31))
print('Second part: {} * {} * {} * {} * {} = {}'.format(tree_11, tree_31, tree_51, tree_71, tree_12, tree_11 * tree_31 * tree_51 * tree_71 * tree_12))
