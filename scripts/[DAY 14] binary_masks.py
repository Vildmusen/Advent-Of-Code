from utils import *
import time

input = read_file_strings("inputs/day_14_input.txt")

mem = [None] * 999999
mask = 'X'* 36


# Part 1
def run_part1(input):
    for row in input:
        parts = row.split(' = ')
        if(parts[0] == 'mask'):
            update_mask(parts[1])
        else:
            mem_loc = int(parts[0].split('[')[1][:-1])
            val = convert_with_mask(int(parts[1]))
            mem[mem_loc] = int(val)
         

def update_mask(values):
    print("updating mask:", values)
    global mask
    mask = values


def convert_with_mask(val):
    val_b = str(bin(val))[2:].zfill(36)
    res = ""
    for i, sign in enumerate(mask):
        if(sign == '1'):
            res += '1'
        elif(sign == '0'):
            res += '0'
        else:
            res += val_b[i]
    print("original value:", val, "\t - masked value:", int(res, 2))
    return int(res, 2)


# Part 2
def run_part2(input):
    for row in input:
        parts = row.split(' = ')
        if(parts[0] == 'mask'):
            update_mask(parts[1])
        else:
            mem_locs = convert_with_mask_2(int(parts[0].split('[')[1][:-1]))
            val = int(parts[1])
            for loc in mem_locs:
                update_mem(mem, int(loc, 2), int(val))


def update_mem(mem, loc, value):
    for m in mem:
        if(m[0] == loc):
            m[1] = value
            return
    mem.append([loc, value])


def convert_with_mask_2(val):
    val_b = str(bin(val))[2:].zfill(36)
    res = ""
    floating = []
    locations = []
    locations.append("")
    val = ""
    for j, sign in enumerate(mask):
        if(sign == '1'):
            for i in range(len(locations)):
                val = locations[i] + '1'
                locations[i] = val
        elif(sign == '0'):
            for i in range(len(locations)):
                val = locations[i] + val_b[j]
                locations[i] = val
        elif(sign == 'X'):
            b = []
            for i in locations:
                b.extend([i, i])
            locations = b
            for i, val in enumerate(locations):
                if(i % 2 == 0):
                    locations[i] = val + '1'
                else:
                    locations[i] = val + '0'
    return locations


def build_bin_nums(string):
    res = []
    cur = ""
    for val in string:
        if(val == 'X'):
            res.append()
        else:
            cur += val


starttime = time.perf_counter()

run_part1(input)
print("Answer:", sum([n for n in mem if n != None]), "\n")
mem = []
mask = 'X'* 36
print("Part 2:")
run_part2(input)
print("Answer:", sum([n[1] for n in mem if n != None]))

print("Total execution time:", time.perf_counter() - starttime)