from utils import *
import time

input = read_file_ints("day_1_input.txt")

def find_2_matching(input, sum):
    cur = 1
    for num1 in input:
        for num2 in input[cur:]:
            if(int(num1) + int(num2) == sum):
                return int(num1), int(num2)
            elif(int(num1) + int(num2) > sum):
                break
        cur += 1

def find_3_matching(input, sum):
    cur = 1
    for num1 in input:
        target = sum - int(num1)
        res = find_2_matching(input[cur:], target)
        if(res):
            return num1, res 
        cur += 1

starttime = time.time()
input_sorted = sorted(input)

num1, num2 = find_2_matching(input_sorted, 2020)
print(f"The numbers adding up to 2020 are: {num1} and {num2}")
print("The answer to part 1 is:", int(num1) * int(num2))

num1, num2_3 = find_3_matching(input_sorted, 2020)
print(f"The numbers adding up to 2020 are: {num1}, {num2_3[0]} and {num2_3[1]}")
print("The answer to part 2 is:", int(num1) * int(num2_3[0]) * int(num2_3[1]))

endtime = time.time()

print("Total execution time:", endtime - starttime)