from utils import *
import time

input = read_file_strings("day_5_input.txt")

def calculate_all_seats(input):
    # Part 1
    highest = 0
    all_seats = []
    for row in input:
        row_nr = string_to_binary_to_int(row[:7], 'B', 'F')
        col_nr = string_to_binary_to_int(row[-3:], 'R', 'L')
        cur = (row_nr * 8) + col_nr
        all_seats.append(cur)
        if(cur > highest):
            highest = cur
    # Part 2
    cur_sorted = sorted(all_seats)
    current = cur_sorted[0]
    for num in cur_sorted[1:]:
        if(num == current + 1):
            current = num
        else:
            current += 1
            break
    return highest, current
    

def string_to_binary_to_int(string, high_char, low_char):
    res = ""
    for c in string:
        if(c == high_char):
            res += '1'
        if(c == low_char):
            res += '0'
    return int(res, 2)


starttime = time.time()

res1, res2 = calculate_all_seats(input)
print("Hisghest seat ID is:", res1)
print(res2)

endtime = time.time()

print("Total execution time:", endtime - starttime)