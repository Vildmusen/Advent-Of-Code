from utils import *
import time

input = read_file_strings("inputs/day_13_test.txt")

# Part 1
def check_busses_departures(cur_time, input):
    busses = [row for row in input.split(',') if row != 'x']
    departures = []
    calc_busses = []
    for bus in busses:
        bus_nr = int(bus)
        mod = cur_time % bus_nr
        departures.append(cur_time + (bus_nr - mod))
        calc_busses.append(bus_nr)
    return departures, calc_busses

# Part 2
def check_busses_part2(input):
    busses = []
    for i, row in enumerate(input.split(',')):
        if(row != 'x'):
            busses.append((i, row))
    return check_chinese_mod(busses)


def mult_list(m_list):
    ans = 1
    for val in m_list:
        ans *= int(val)
    return ans


def check_chinese_mod(busses):
    n = [int(bus[1]) for bus in busses]
    a = [int(bus[0]) for bus in busses]

    big_n = mult_list(n)
    
    z = []
    y = []

    for n_i in n:
        y.append(big_n/n_i)

    for i, val in enumerate(n):
        res, m1, m2 =  gcd_extended(y[i], val)
        z.append(y[i] + m2)

    res = 0
    for i, val in enumerate(a):
        res += val * z[i] * y[i]
    final = res % big_n

    return n, a, y, z, res, final


def gcd_extended(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = gcd_extended(b % a, a)  
    
    # Update x and y using results of recursive  
    # call
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 


starttime = time.perf_counter()

dep, bus = check_busses_departures(int(input[0]), input[1])
min_wait = min(dep)
index = dep.index(min_wait)
print((min_wait - int(input[0])) * bus[index])

res = check_busses_part2(input[1])
print(res)

print("Total execution time:", time.perf_counter() - starttime)