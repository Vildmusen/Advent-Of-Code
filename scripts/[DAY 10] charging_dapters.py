from utils import *
import time

input = read_file_ints("inputs/day_10_input.txt")

# Part 1
def check_differences(sorted_input):
    return [sorted_input[i+1]-val for i, val, in enumerate(sorted_input) if i < len(sorted_input)-1]


# Part 2
def check_connections(input):
    if(len(input) < 1):
        return 1
    len_1s_repeating = check_repeating_ones(input)
    return fib_3(len_1s_repeating) * check_connections(input[len_1s_repeating:])


def fib_3(size):
    if(size == 2):
        return 1
    if(size == 1):
        return 1
    if(size == 0):
        return 0
    else:
        return fib_3(size-1) + fib_3(size-2) + fib_3(size-3)


def check_repeating_ones(input):
    for i in range(len(input)-1):
        if(input[i] + 1 != input[i+1]):
            return i + 1
    return len(input)


# RUN
starttime = time.perf_counter()

input_sorted = sorted(input)
input_sorted.insert(0,0)
input_sorted.append(max(input_sorted)+3)

res = check_differences(input_sorted)
print(f"Part 1: 1-off; {res.count(1)}, 3-off: {res.count(3)}, Result: {res.count(1)*res.count(3)}")
res2 = check_connections(input_sorted)
print(f"Part 2: Total amount of permutations: {res2}")

print("Total execution time:", time.perf_counter() - starttime)