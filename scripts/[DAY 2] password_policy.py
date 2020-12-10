from utils import *
import time

input = read_file_strings("day_2_input.txt")

def check_password_valid_rule_1(rangelow, rangehigh, char, password):
    count = 0
    for c in password:
        if(c == char):
            count += 1
        if(count > rangehigh):
            return False
    return count >= rangelow


def check_password_valid_rule_2(pos1, pos2, char, password):
    a = password[pos1] == char
    b = password[pos2] == char
    return (a and not b) or (not a and b)


def check_all_passwords(input):
    count1 = 0
    count2 = 0
    for i in input:
        parts = i.split(':')
        range = parts[0][:-2].split('-')
        if(check_password_valid_rule_1(int(range[0]), int(range[1]), parts[0][-1], parts[1])):
            count1 += 1
        if(check_password_valid_rule_2(int(range[0]), int(range[1]), parts[0][-1], parts[1])):
            count2 += 1
    return count1, count2


starttime = time.time()
res1, res2 = check_all_passwords(input)
print("The number of valid passwords for rule 1 are:", res1)
print("The number of valid passwords for rule 2 are:", res2)
endtime = time.time()

print("Total execution time:", endtime - starttime)