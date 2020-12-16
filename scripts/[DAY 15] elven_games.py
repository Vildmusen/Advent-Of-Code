from utils import *
import time

input = read_file_strings("inputs/day_15_test.txt")

def play1(input, length):
    nr_arr = [int(nr) for nr in input[0].split(',')]
    nrs = len(nr_arr)
    while(nrs < length):
        cur = nr_arr[nrs - 1]
        if(cur in nr_arr[:-1]):
            i = max([pos for pos, val in enumerate(nr_arr[:-1]) if val == cur])
            nr_arr.append(nrs - (i + 1))
        else:
            nr_arr.append(0)
        nrs += 1
    return nr_arr[length - 1]


def play2(input, length):
    nr_dict = {}
    starting_nums = [int(val) for val in input[0].split(',')]
    for pos, nr in enumerate(starting_nums):
        nr_dict[int(nr)] = pos
    nr_dict[0] = 0
    last_spoken = starting_nums[-1]
    temp = starting_nums[:-1]
    cur_i = len(nr_dict) - 1
    while(cur_i < length):
        temp.append(last_spoken)
        if(last_spoken in nr_dict):
            if(nr_dict[last_spoken] != cur_i - 1):
                last_pos = nr_dict[last_spoken]
                last_spoken = cur_i - last_pos
                nr_dict[last_spoken] = cur_i
            else:
                last_spoken = 0
        else:
            last_spoken = 0
            nr_dict[last_spoken] = cur_i
            
        cur_i += 1
    return temp

starttime = time.perf_counter()
print("Starting with:", input)
res = play1(input, 2020)
print(f"nr {res} is the 2020th!")
res = play2(input, 2020)
print(f"nr {res} is the 30000000th!")
print("Total execution time:", time.perf_counter() - starttime)