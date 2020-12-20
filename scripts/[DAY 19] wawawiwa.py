from utils import read_file_strings
import time

input = read_file_strings("inputs/day_19_input.txt")

def build_rule(rules):
    while(has_numbers(rules[0])):
        for key in rules:
            rules = replace_all(rules, key, rules[key])
    return rules[0]


def replace_all(rules, num, key_rules):
    length = len(key_rules)
    for key in rules:
        new_rules = []
        for rule in rules[key]:
            if(str(num) in rule):
                for i in range(length):
                    new = ""
                    for char in rule:
                        if(char == str(num)):
                            new += key_rules[i]
                        else:
                            new += char
                    new_rules.append(new)
            else:
                new_rules.append(rule)
        rules.update({key:new_rules})
    return rules


def has_numbers(rule_list):
    for row in rule_list:
        for char in row:
            if(not(char == "a" or char == "b")):
                return True
    return False


def find_matching(rules, input_rows):
    count = 0
    correct = []
    for row in input_rows:
        if(row in rules):
            count += 1
            correct.append(row)
    return count, correct

starttime = time.perf_counter()

rules = input[:input.index("")]
input_rows = input[input.index("") + 1:]

rule_dict = {}

for rule in rules:
    parts = rule.split(':')
    piped_rules = parts[1].split('|')
    all_rules = []
    for rule in piped_rules:
        all_rules.append(rule.replace(' ','').replace('"', ''))
    rule_dict[int(parts[0])] = all_rules

res = build_rule(rule_dict)

print("Possible rows:", res)

res2, rows = find_matching(res, input_rows)

for row in rows:
    print(row)
print("Nr rows mathcing:", res2)

print("Total execution time:", time.perf_counter() - starttime)