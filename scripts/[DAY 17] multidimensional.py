from utils import *
import time

input = read_file_strings("inputs/day_17_input.txt")


# Part 1
def run_simulation(layers, cycles):
    count = 0
    while(count < cycles):
        layers = add_layers(layers)
        layers = check_rules(layers)
        print_current(layers)
        count += 1
    active_cubes = 0
    for key in layers.keys():
        for row in layers[key]:
            active_cubes += row.count('#')
    return active_cubes


def add_layers(layers):
    cur_min = min(layers.keys())
    cur_max = max(layers.keys())
    size_x = len(layers[cur_min]) + 2
    size_y = len(layers[cur_max][0]) + 2

    # Expand current z's
    for z in layers.keys():
        new_arr = []
        empty_row = ""
        for i in range(size_x):
            empty_row += "."
        new_arr.append(empty_row)
        cur = layers[z]
        for row in cur:
            new_arr.append('.' + row + '.')
        new_arr.append(empty_row)
        layers.update({z: new_arr})        


    # Add new outer z's
    new_layer = []
    for i in range(size_x):
        new_row = ""
        for j in range(size_y):
            new_row += '.'
        new_layer.append(new_row)

    layers[cur_min - 1] = new_layer
    layers[cur_max + 1] = new_layer

    return layers


def check_rules(layers):
    new_layers = {}
    for z in range(max(layers.keys())+1):
        cur = layers.get(z)
        new_layer_arr = []
        for y, row in enumerate(cur):
            new_row = ""
            for x, char in enumerate(row):
                nearby_active = count_neighbors(layers, x, y, z)
                if(char == '#'):
                    nearby_active -= 1
                    if(nearby_active == 2 or nearby_active == 3):
                        new_row += '#'
                    else:
                        new_row += '.'
                if(char == '.'):
                    if(nearby_active == 3):
                        new_row += '#'
                    else:
                        new_row += '.'
            new_layer_arr.append(new_row)
        new_layers[z] = new_layer_arr
    for z in range(min(layers.keys()), 0):
        new_layers[z] = new_layers[-z]
    return new_layers
        

def count_neighbors(layers, x, y, z):
    count = 0
    for z_pos in range(z-1, z+2):
        for y_pos in range(y-1, y+2):
            for x_pos in range(x-1, x+2):
                cur = layers.get(z_pos)
                if(cur != None):
                    try:
                        if(cur[y_pos][x_pos] == '#'):
                            count += 1
                    except IndexError:
                        do = "nothing"    
    return count


def print_current(layers):
    for i in range(min(layers.keys()), max(layers.keys())+1):
        cur = layers.get(i)
        print(f"\nz={i}")
        for row in cur:
            print(row)


# Part 2
def run_simulation2(layers, cycles):
    count = 0
    z = 0
    w = 0
    while(count < cycles):
        layers = add_layers2(layers, z, w)
        layers = check_rules2(layers, z, w)
        print_current2(layers)
        count += 1
        z += 1
        w += 1
    active_cubes = 0
    for key in layers.keys():
        for row in layers[key]:
            active_cubes += row.count('#')
    return active_cubes


def add_layers2(layers, cur_min, cur_max):
    size_x = len(layers[(0,0)]) + 2
    size_y = len(layers[(0,0)][0]) + 2

    # Expand current z's
    for z in layers.keys():
        new_arr = []
        empty_row = ""
        for i in range(size_x):
            empty_row += "."
        new_arr.append(empty_row)
        cur = layers[z]
        for row in cur:
            new_arr.append('.' + row + '.')
        new_arr.append(empty_row)
        layers.update({z: new_arr})        

    # Add new w's and z's
    new_layer = []
    for i in range(size_x):
        new_row = ""
        for j in range(size_y):
            new_row += '.'
        new_layer.append(new_row)

    for z in range(0 - (cur_min + 1), cur_max + 2):
        for w in range(0 - (cur_min + 1), cur_max + 2):
            if(layers.get((z,w)) == None):
                layers[(z, w)] = new_layer

    return layers


def check_rules2(layers, z_i, w_i):
    new_layers = {}
    for z in range(0 - (z_i + 1), z_i + 2):
        for w in range(0 - (w_i + 1), w_i + 2):
            cur = layers.get((z,w))
            new_layer_arr = []
            for y, row in enumerate(cur):
                new_row = ""
                for x, char in enumerate(row):
                    nearby_active = count_neighbors2(layers, x, y, z, w)
                    if(char == '#'):
                        nearby_active -= 1
                        if(nearby_active == 2 or nearby_active == 3):
                            new_row += '#'
                        else:
                            new_row += '.'
                    if(char == '.'):
                        if(nearby_active == 3):
                            new_row += '#'
                        else:
                            new_row += '.'
                new_layer_arr.append(new_row)
            new_layers[(z,w)] = new_layer_arr
    return new_layers
        

def count_neighbors2(layers, x, y, z, w):
    count = 0
    for z_pos in range(z-1, z+2):
        for w_pos in range(w-1, w+2):
            for y_pos in range(y-1, y+2):
                for x_pos in range(x-1, x+2):
                    cur = layers.get((z_pos, w_pos))
                    if(cur != None):
                        try:
                            if(cur[y_pos][x_pos] == '#'):
                                count += 1
                        except IndexError:
                            do = "nothing"    
    return count


def print_current2(layers):
    for key in layers.keys():
        print("\n",key)
        for row in layers[key]:
            print(row)

starttime = time.perf_counter()

# layers = {}
# layers[0] = input
# res = run_simulation(layers, 6)
# print("Nr of active cubes:", res)

layers = {}
layers[(0,0)] = input
res = run_simulation2(layers, 6)
print("Nr of active cubes:", res)

print("Total execution time:", time.perf_counter() - starttime)