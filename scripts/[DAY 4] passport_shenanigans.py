from utils import *
import time

input = read_file_strings("day_4_input.txt")

def check_passports(input):
    current = []
    count = 0
    for row in input:
        if(row == ''):
            if(check_valid(current)):
                count += 1
            current = []
        else:
            key_values = row.split()
            for pair in key_values:
                current.append(pair)
    # check last row as well
    if(check_valid(current)):
        count += 1
    return count

def check_valid(current):
    if(not check_fields_existing(current)):
        return False

    for field in current:
        key, value = field.split(':')
        if(key == 'byr' and not check_int(value, 1920, 2002)):
            return False
        if(key == 'iyr' and not check_int(value, 2010, 2020)):
            return False
        if(key == 'eyr' and not check_int(value, 2020, 2030)):
            return False
        if(key == 'hgt' and not check_height(value)):
            return False
        if(key == 'hcl' and not check_hex(value)):
           return False
        if(key == 'ecl' and not check_color(value)):
            return False
        if(key == 'pid' and not check_number_format(value)):
            return False
    return True

def check_fields_existing(current):
    if(len(current) < 7):
        return False
    if(len(current) == 7):
        for field in current:
            if('cid' in field):
                return False
    return True

def check_int(value, low, high):
    return int(value) >= low and int(value) <= high

def check_number_format(value):
    return value.isnumeric() and len(value) == 9

def check_hex(value):
    try:
        if(value[0] != "#" or len(value) != 7):
            return False
        hexnr = value[-6:]
        test = int(hexnr, 16)
        return True
    except Exception:
        return False

def check_height(value):
    unit = value[-2:]
    if(not(unit == "in" or unit == "cm")):
        return False
    val = value[:-2]
    if(unit == 'in'):
        return check_int(val, 59, 76)
    if(unit == 'cm'):
        return check_int(val, 150, 193)
    print("what")
    return True

def check_color(value):
    return value in ['amb','blu','brn','gry','grn','hzl','oth']


starttime = time.time()

res = check_passports(input)
print("Total number of valid passports are: ", res)

endtime = time.time()

print("Total execution time:", endtime - starttime)