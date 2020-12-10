from utils import *
import time
import pandas as pd

input = read_file_ints("day_9_input.txt")

# Part 1
def check_valid_numbers(p_length, input):
    for i, num in enumerate(input[p_length:]):
        if(not check_valid_number(input[i:][:p_length], num)):
            return num


def check_valid_number(factors, num):
    for f in factors:
        if(num - f in factors):
            return True
    return False


# Part 2
def find_range(invalid_num, input):
    for index, num in enumerate(input):
        success, end_index = test_num(invalid_num, index, 0)
        if(success):
            sliced_input = input[index:end_index]
            return min(sliced_input) + max(sliced_input)


def test_num(invalid_num, index, sum):
    if(sum > invalid_num):
        return False, index
    if(sum == invalid_num):
        return True, index
    sum += input[index]
    index += 1
    return test_num(invalid_num, index, sum)


# RUN 
starttime = time.time()
res = check_valid_numbers(25, input)
print("First invalid number is:", res)
res2 = find_range(res, input)
print("results 2 is:", res2)
endtime = time.time()
print("Total execution time:", endtime - starttime)