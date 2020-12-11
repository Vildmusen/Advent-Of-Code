from utils import *
import time
import os


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
    new = cycle_seats_v3(input)
    old = input
    while(old != new):
        old = new
        new = cycle_seats_v3(new)
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in new:
            special_row = ""
            for char in row:
                if(char == 'L'):
                    special_row += '[_]'
                if(char == '#'):
                    special_row += '[Ö]'
                if(char == '.'):
                    special_row += '___'
            print(special_row)
        time.sleep(0.2)
    return new


def cycle_seats_v3(input):
    new_arr = []
    for x, row in enumerate(input):
        new_row = ""
        for y, seat in enumerate(row):
            if(seat == 'L'):
                if(adj_seats_on_line(x,y,input) == 0):
                    new_row += '#'
                else:
                    new_row += 'L'
            elif(seat == '#'):
                if(adj_seats_on_line(x,y,input) > 4):
                    new_row += 'L'
                else:
                    new_row += '#'
            else:
                new_row += '.'
        new_arr.append(new_row)
    return new_arr


def adj_seats_on_line(x,y,input):
    count = 0
    count += check_line(x,y,input,-1, 0)    # up
    count += check_line(x,y,input,0, 1)     # right
    count += check_line(x,y,input,1, 0)     # down
    count += check_line(x,y,input,0, -1)    # left
    count += check_line(x,y,input,-1, -1)   # diagonal up right
    count += check_line(x,y,input,-1, 1)    # diagonal up left
    count += check_line(x,y,input,1, 1)     # diagonal down right
    count += check_line(x,y,input,1, -1)    # diagonal down left    
    return count


def check_line(x, y, input, dir_x, dir_y):
    min = 0
    x_max = len(input)
    y_max = len(input[0])
    dist = 1
    x_d = (dir_x * dist)
    y_d = (dir_y * dist)
    while(x + x_d < x_max and x + x_d >= min and y + y_d < y_max and y + y_d >= min):
        cur = input[x + x_d][y + y_d]
        if(cur == '#'):
            return 1
        if(cur == 'L'):
            return 0
        dist += 1
        x_d = (dir_x * dist)
        y_d = (dir_y * dist)
    return 0

starttime = time.perf_counter()

input = list(input)
print("\nInitial grid:")
for row in input:
    print(row)

# generated_seating = run_seat_cycle(input)
# print("\nFinished grid part 1:")
# count = 0
# for row in generated_seating:
#     count += row.count('#')
#     print(row)
# print("Number of occupied seats:", count)

generated_seating = run_seat_cycle_v2(input)
print("\nFinished grid part 2:")
count = 0
for row in generated_seating:
    count += row.count('#')
    print(row)
print("Number of occupied seats:", count)

print("Total execution time:", time.perf_counter() - starttime)