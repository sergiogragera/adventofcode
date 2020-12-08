import math


def bin_search(c, min_max_col):
    binary = (min_max_col[0] + min_max_col[1]) / 2.0
    if c is 'F' or c is 'L':
        min_max_col = [min_max_col[0], int(binary)]
    else:
        min_max_col = [int(math.ceil(binary)), min_max_col[1]]
    return min_max_col


def get_row_col(line):
    min_max_row = [0, 127]
    min_max_col = [0, 7]
    for c in line[:-5]:
        min_max_row = bin_search(c, min_max_row)
    for c in line[-4:-2]:
        min_max_col = bin_search(c, min_max_col)
    return (min_max_row[0 if line[6] is 'F' else 1], min_max_col[0 if line[-2] is 'L' else 1])


with open('resources/day5.data') as file:
    max_seat_id = 0
    seats = []
    possible_seats = []
    for line in file:
        row, col = get_row_col(line)
        seat_id = row * 8 + col
        for s in seats:
            if math.fabs(s - seat_id) == 2:
                possible_seats.append((s + seat_id) / 2)
        seats.append(seat_id)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    print('First part: max seat ID {}.'.format(max_seat_id))
    for ps in possible_seats:
        if ps not in seats:
            print('Second part: your seat ID is {}.'.format(ps))
