from utils import *
import time

input = read_file_strings("inputs/day_11_input.txt")


# Part 1
def run_seat_cycle(input):
    input = add_spaces(input)
    new = cycle_seats_v2(input)
    old = input
    while(old != new):
        old = new
        new = cycle_seats_v2(new)
    return new


def cycle_seats_v2(input):
    new_arr = []
    for x, row in enumerate(input):
        new_row = ""
        for y, seat in enumerate(row):
            if(seat == 'L'):
                adj_list = input[x-1][y-1:y+2] + input[x][y-1:y+2] + input[x+1][y-1:y+2]
                if(adj_list.count('#') == 0):
                    new_row += '#'
                else:
                    new_row += 'L'
            elif(seat == '#'):
                adj_list = input[x-1][y-1:y+2] + input[x][y-1:y+2] + input[x+1][y-1:y+2]
                if(adj_list.count('#') - 1 > 3):
                    new_row += 'L'
                else:
                    new_row += '#'
            else:
                new_row += '.'
        new_arr.append(new_row)
    return new_arr


def add_spaces(input):
    new_arr = []
    new_size = len(input[0]) + 2
    new_arr.append(''.join(['.'*new_size]))
    for row in input:
        new = '.'
        for char in row:
            new += char
        new += '.'
        new_arr.append(new)
    new_arr.append(''.join(['.'*new_size]))
    return new_arr


# Part 2
def run_seat_cycle_v2(input):
    input = add_spaces(input)
    new = cycle_seats_v2(input)
    old = input
    while(old != new):
        old = new
        new = cycle_seats_v2(new)
    return new

starttime = time.perf_counter()

input = list(input)
print("\nInitial grid:")
for row in input:
    print(row)

generated_seating = run_seat_cycle(input)
print("\nFinished grid part 1:")
count = 0
for row in generated_seating:
    count += row.count('#')
    print(row)
print("Number of occupied seats:", count)

generated_seating = run_seat_cycle_v2(input)
print("\nFinished grid part 2:")
count = 0
for row in generated_seating:
    count += row.count('#')
    print(row)
print("Number of occupied seats:", count)

print("Total execution time:", time.perf_counter() - starttime)