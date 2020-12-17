from utils import *
import time

input = read_file_strings("inputs/day_15_input.txt")

def play(input, length):
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


def play_fast(count, num, nr_dict, length):
    wow_it_was_said_before = False
    while(count < length - 1):
        mem = nr_dict.get(num)
        if(mem == None):
            nr_dict[num] = count
            num = 0
        else:
            nr_dict.update({num:count})
            num = count - mem
        count += 1
    return num


starttime = time.perf_counter()
print("Starting with:", input)
res = play(input, 2020)
print(f"nr {res} is the 2020th!")
print("Time since start:", time.perf_counter() - starttime)

nr_dict = {}
for i, val in enumerate(input[0].split(",")[:-1]):
    nr_dict[int(val)] = i
num_arr = [int(val) for val in input[0].split(',')]
res = play_fast(len(num_arr)-1, num_arr[-1:][0], nr_dict, 30000000)
print(f"nr {res} is the 30000000th!")
print("Total execution time:", time.perf_counter() - starttime)