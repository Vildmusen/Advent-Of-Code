from utils import *
import time

input = read_file_strings("inputs/day_16_input.txt")

def concat_valid_numbers(rules):
    all_valid_numbers = []
    for val in rules:
        ranges = val.split(":")[1].split("or")
        for range in ranges:
            nums = range.split("-")
            low = int(nums[0])
            high = int(nums[1])
            cur = low
            while(cur <= high):
                all_valid_numbers.append(cur)
                cur += 1
    return list(set(all_valid_numbers))


def concat_valid_numbers_per_rule(rules):
    all_valid_numbers_dict = {}
    for val in rules:
        ranges = val.split(":")[1].split("or")
        for range in ranges:
            nums = range.split("-")
            low = int(nums[0])
            high = int(nums[1])
            rule_arr = []
            cur = low
            while(cur <= high):
                rule_arr.append(cur)
                cur += 1
            cur_pos = val.split(':')[0]
            if(cur_pos in all_valid_numbers_dict):
                cur = all_valid_numbers_dict[cur_pos]
                for val in rule_arr:
                    cur.append(val)
                all_valid_numbers_dict.update({cur_pos:cur})
            else:
                all_valid_numbers_dict[cur_pos] = rule_arr
    return all_valid_numbers_dict


def check_valid_tickets(all_nums, tickets):
    error_rate = 0
    correct = True
    good_tickets = []
    for ticket in tickets:
        for num in ticket.split(","):
            if(not int(num) in all_nums):
                error_rate += int(num)
                correct = False
        if(correct):
            good_tickets.append(ticket)
        correct = True

    return error_rate, good_tickets

def check_valid_fields_for_tickets(tickets, field_rules):
    ticket_pos = []
    for i in range(len(tickets[0].split(","))):
        ticket_pos.append([])
    for i, ticket in enumerate(tickets):
        for i, field in enumerate(ticket.split(",")):
            fields = []
            for rule in field_rules:
                field = int(field)
                if(field in field_rules[rule]):
                    fields.append(rule)
            cur = ticket_pos[i]
            cur.append(fields)
            ticket_pos[i] = cur
    return ticket_pos


def check_valid(fields, length):
    correct_fields = {}
    for i, val in enumerate(fields):
        possibilities = []
        correct = []
        for field in val:
            for f in field:
                possibilities.append(f)
        for fff in list(set(possibilities)):
            if(possibilities.count(fff) == length):
                correct.append(fff)        
        correct_fields[i] = correct
    return correct_fields

def check_correct_res(pos_dict):
    abs_correct = {}
    still_not_sure = True
    while(still_not_sure):
        for key in pos_dict.keys():
            val = pos_dict[key]
            if(len(val) == 1):
                val = val[0]
                abs_correct[key] = val
                for key2 in pos_dict.keys():
                    cur = pos_dict[key2]
                    if(val in cur):
                        cur.remove(val)
                        pos_dict.update({key2:cur})
        still_not_sure = False
        for val in pos_dict.values():
            if(len(val) > 1):
                still_not_sure = True
    return abs_correct


starttime = time.perf_counter()

first_split = input.index('')
rules = input[:first_split]
second_split = input[first_split + 1:].index('')
nearby = input[first_split + 1:][second_split + 1:][1:]
print(rules)

all_valid_numbers = concat_valid_numbers(rules)
res, new_tickets = check_valid_tickets(all_valid_numbers, nearby)
print("Error rate:", res)
print(new_tickets)

my_ticket = '109,199,223,179,97,227,197,151,73,79,211,181,71,139,53,149,137,191,83,193'.split(',')

all_valid_numbers_pers_rule = concat_valid_numbers_per_rule(rules)
res = check_valid_fields_for_tickets(new_tickets, all_valid_numbers_pers_rule)
resres = check_valid(res, len(new_tickets))
for val in resres:
    print(resres[val])

resresres = check_correct_res(resres)

sum = 1
for i in resresres.keys():
    if('departure' in resresres[i]):
        sum *= int(my_ticket[i])

print(sum)

print("Total execution time:", time.perf_counter() - starttime)