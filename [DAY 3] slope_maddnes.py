from utils import *
import time

input = read_file_strings("day_3_input.txt")

def check_impacts(input, width, step):
    x = 0
    count = 0
    for i in input:
        pos = x % width
        if(i[pos] == '#'):
            count += 1
        x += step
    return count

def get_half(arr):
    count = 0
    res = []
    for i in arr:
        if(count % 2 == 0):
            res.append(i)
        count += 1
    return res

starttime = time.time()

width = len(input[0])

res1_1 = check_impacts(input, width, 1)
res1_3 = check_impacts(input, width, 3)
res1_5 = check_impacts(input, width, 5)
res1_7 = check_impacts(input, width, 7)

input_half = get_half(input)

res2_1 = check_impacts(input_half, width, 1)

print("Total number of trees impacted:", res1_3)

res_total = res1_1 * res1_3 * res1_5 * res1_7 * res2_1

print("Final factor:", res_total)

endtime = time.time()

print("Total execution time:", endtime - starttime)