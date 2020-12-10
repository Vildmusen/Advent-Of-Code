from utils import *
import time
import numpy as np

input = read_file_strings("day_7_input.txt")


# PART 1
def check_all_bags(input):
    bag_colors = []
    last = 0
    valid_bags = ['shiny gold bags']
    size = len(valid_bags)
    while(size != last):
        for row in input:
            valid_bags = add_new_colors(row, valid_bags)
        last = size
        size = len(valid_bags)
    return len(valid_bags) - 1


def add_new_colors(row, valid_bags):
    if('contain' in row):
        outer, inner = row.split('contain')
        inner_bags = inner.split(',')
        inner_bags_cleaned = [" ".join(bag.split(' ')[2:4]) + ' bags' for bag in inner_bags]
        if(np.any(np.in1d(inner_bags_cleaned, valid_bags))):
            valid_bags.append(" ".join(outer.split(' ')[:3]))
            valid_bags = list(set(valid_bags))
        return valid_bags


# PART 2
def check_bags_inside(bag):
    '''
    Makes list of inner bags ['2 big red','4 lustrous beige'] etc..
    Finds inner bags result recursively and add to total with (cur_bag_count * inner bag total)
    Returns (inner bag total + self)
    '''
    inner = bag.split('contain')[1]
    inner_bags_cleaned = [" ".join(bag.split(' ')[1:4]) for bag in inner.split(',')] 
    if(inner == ' no other bags.'):
        return 1
    count = 0
    for bag in inner_bags_cleaned:
        bag_words = bag.split(' ')
        cur_bag_count = int(bag_words[0])
        bag_name = " ".join(bag_words[1:3]) + ' bags '
        count += cur_bag_count * check_bags_inside(get_bag_on_name(bag_name)) 
    return count + 1 


def get_bag_on_name(name):
    return [bag for bag in input if bag.split('contain')[0] == name][0]


# RUN 
starttime = time.time()
res1 = check_all_bags(input)
res2 = check_bags_inside(get_bag_on_name('shiny gold bags '))
print(res1)
print(res2 - 1)
endtime = time.time()
print("Total execution time:", endtime - starttime)