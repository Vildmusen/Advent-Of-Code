from utils import *
import time
import math

input = read_file_strings("inputs/day_13_input.txt")

# Part 1
def check_busses_departures(cur_time, input):
    busses = [row for row in input.split(',') if row != 'x']
    departures = []
    calc_busses = []
    for bus in busses:
        bus_nr = int(bus)
        mod = cur_time % bus_nr
        departures.append(cur_time + (bus_nr - mod))
        calc_busses.append(bus_nr)
    return departures, calc_busses

# Part 2
def check_busses_part2(input):
    busses = []
    for i, row in enumerate(input.split(',')):
        if(row != 'x'):
            busses.append((i, row))
    return find_t(busses)


def find_t(busses):
    # Build mods and remainders
    rems = []
    mods = []
    for rem, mod in busses:
        rem -= int(mod)
        while(rem > 0):
            rem -= int(mod)
        rems.append(abs(rem))
        mods.append(int(mod))
    rems[0] = 0
    print(rems, mods, "\n")

    # Initial values
    all_good = False
    count = 1
    prev = 0
    nr = 1
    inc = 1
    iterations = 0

    # loop until t is found
    while(not all_good):
        all_good = True
        for i, val in enumerate(rems):
            if(count % mods[i] != val):
                if(i > nr):
                    if(prev != 0):
                        inc = count - prev
                        print(f"Found 2 chains of {nr}, increasing increment to: \n{count}-{prev} =", inc, "\n")
                        prev = 0
                        nr += 1
                    else:
                        prev = count
                all_good = False
                break
        count += inc
        iterations += 1
        if(iterations % 10000000 == 0):
            print(f"Progress: ({count})")
    return count - inc


starttime = time.perf_counter()

dep, bus = check_busses_departures(int(input[0]), input[1])
min_wait = min(dep)
index = dep.index(min_wait)
print((min_wait - int(input[0])) * bus[index])

res = check_busses_part2(input[1])
# res = fuck_it(input[1], 0)
print(res, "was correct")

print("Total execution time:", time.perf_counter() - starttime)