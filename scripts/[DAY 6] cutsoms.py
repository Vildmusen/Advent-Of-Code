from utils import *
import time

input = read_file_strings("day_6_test.txt")

def check_all_groups(input):
    group = []
    count = 0
    for row in input:
        if(row != ''):
            group.append(list(row))
            count += 1
        else:
            print(group)
            print(count)
            group = []
            count = 0

'''
def check_all_groups(input):
    next = []
    groups = []
    count = 0
    for row in input:
        if(row == ''):
            score = 0
            for char in set(next):
                if(next.count(char) == count):
                    score += 1
            groups.append(score)
            count = 0
            next = []
        else:
            count += 1
            row_chars = list(row)
            for char in row_chars:
                next.append(char)
    score = 0
    for char in set(next):
        if(next.count(char) == count):
            score += 1
    groups.append(score)
    count = 0
    return sum(groups)
'''
            
starttime = time.time()

res = check_all_groups(input)
print(res)

endtime = time.time()

print("Total execution time:", endtime - starttime)