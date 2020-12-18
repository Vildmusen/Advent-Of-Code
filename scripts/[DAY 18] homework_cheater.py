from utils import *
import time

input = read_file_strings("inputs/day_18_input.txt")


# Part 1
def calculate_no_rules(row):
    sum = 0
    skip = 0
    for i, char in enumerate(row):
        if(skip > 0):
            skip -= 1
            continue
        if(char == '('):
            end = find_closing(row[i:])
            if(row[i-1] == '*'):
                sum *= calculate_no_rules(row[i+1:i+end])
            else:
                sum += calculate_no_rules(row[i+1:i+end])
            skip = end
        else:
            if(i == 0):
                sum += int(char)
            elif(row[i-1] == '*'):
                sum *= int(char)
            elif(row[i-1] == '+'):
                sum += int(char)
    return sum
                

def find_closing(row_part):
    depth = 0
    for i, char in enumerate(row_part):
        if(char == '('):
            depth += 1
        if(char == ')'):
            depth -= 1
        if(depth == 0):
            return i


# Part 2
def calculate_add_first(row):
    sum = 0
    skip = 0
    cur = 0
    for i, char in enumerate(row):
        if(skip > 0):
            skip -= 1
            continue
        if(char == '('):
            end = find_closing(row[i:])
            cur = calculate_add_first(row[i+1:i+end])
            skip = end
        elif(char.isdigit()):
            cur = int(char)
        if(i == 0):
            sum += cur
        elif(row[i-1] == '+'):
            sum += cur
        elif(row[i-1] == '*'):
            sum *= calculate_add_first(row[i:])
            return sum
    return sum


starttime = time.perf_counter()

# print(input)
res = []
for row in input:
    row = row.replace(" ", "")
    res.append((row, calculate_no_rules(row)))

totalsum = 0
for row in res:
    # print(row[0], "=", row[1])
    totalsum += row[1]

print("The total sum of all no-rule equations is:", totalsum)

res = []
for row in input:
    row = row.replace(" ", "")
    res.append((row, calculate_add_first(row)))

totalsum = 0
for row in res:
    # print(row[0], "=", row[1])
    totalsum += row[1]

print("The total sum of all addition-first equations is:", totalsum)

print("Total execution time:", time.perf_counter() - starttime)