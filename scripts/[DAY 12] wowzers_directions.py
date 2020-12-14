from utils import *
import time

input = read_file_strings("inputs/day_12_input.txt")

# Part 1
def move_ship(input):
    x = 0
    y = 0
    degree = 0
    for inst in input:
        prefix = inst[0]
        val = int(inst[1:])
        # N,E,S,W
        if(prefix == 'N'):
            y += val
        elif(prefix == 'E'):
            x += val
        elif(prefix == 'S'):
            y -= val
        elif(prefix == 'W'):
            x -= val
        # Turn
        if(prefix == 'L'):
            degree -= val
            degree = degree % 360
        if(prefix == 'R'):
            degree += val
            degree = degree % 360
        # forward
        if(prefix == 'F'):
            if(degree == 0):
                x += val
            elif(degree == 90):
                y -= val
            elif(degree == 180):
                x -= val
            elif(degree == 270):
                y += val
    return x, y


# Part 2
def move_ship_with_waypoint(input):
    ship_x = 0
    ship_y = 0
    way_x = 10
    way_y = 1
    degree = 0
    for inst in input:
        prefix = inst[0]
        val = int(inst[1:])
        # N,E,S,W
        if(prefix == 'N'):
            way_y += val
        elif(prefix == 'E'):
            way_x += val
        elif(prefix == 'S'):
            way_y -= val
        elif(prefix == 'W'):
            way_x -= val
        # Turn
        if(prefix == 'L' or prefix == 'R'):
            print(prefix, val, way_x, way_y)
            if(val == 180):
                way_x = -(way_x)
                way_y = -(way_y)
            if(val == 90 and prefix == 'L' or val == 270 and prefix == 'R'):
                temp = way_x
                way_x = -(way_y)
                way_y = temp
            if(val == 90 and prefix == 'R' or val == 270 and prefix == 'L'):
                temp = way_x
                way_x = way_y
                way_y = -(temp)
            print(way_x, way_y)
        # forward
        if(prefix == 'F'):
            ship_x += val * way_x
            ship_y += val * way_y
        print(f"waypoint: {way_x},{way_y} pointing {degree} degrees from e | ship: {ship_x},{ship_y}")
    return ship_x, ship_y
    

starttime = time.perf_counter()
x,y = move_ship(input)
print(f"Final position of the ship is {x}, {y}, with a manhattan distance of {abs(x)+abs(y)}")
x,y = move_ship_with_waypoint(input)
print(f"Final position of the waypoint is {x}, {y}, with a manhattan distance of {abs(x)+abs(y)}")
print("Total execution time:", time.perf_counter() - starttime)
