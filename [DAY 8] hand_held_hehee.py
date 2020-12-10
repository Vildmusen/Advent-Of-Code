from utils import *
import time
import pandas as pd

input = read_file_strings("day_8_input.txt")

accumulator = 0
ints_pointer = 0
recent_instructions = []

# Part 1
def run(instructions):
    reset()
    return read_next(instructions[ints_pointer], instructions)


def read_next(cur_instruction, instructions):
    global recent_instructions
    global accumulator
    global ints_pointer
    cur_type, val = cur_instruction.split(' ')
    val_int = val_to_int(val)
    if(not ints_pointer in recent_instructions):
        recent_instructions.append(ints_pointer)
    else:
        print(f'Program in loop - exiting. [acc == {accumulator}]')
        return False
    ints_pointer += 1
    try:
        if(cur_type == 'nop'):
            return read_next(instructions[ints_pointer], instructions)
        elif(cur_type == 'acc'):
            accumulator += val_int
            return read_next(instructions[ints_pointer], instructions)
        elif(cur_type == 'jmp'):
            ints_pointer += (val_int - 1)
            return read_next(instructions[ints_pointer], instructions)
    except Exception as ex:
        print(f'Program successfully executed. [acc == {accumulator}]')
        return True


def val_to_int(val):
    if(val[0] == '+'):
        return int(val[1:])
    else:
        return 0 - int(val[1:])


def reset():
    global ints_pointer
    global recent_instructions
    global accumulator
    accumulator = 0
    ints_pointer = 0
    recent_instructions = []

# Part 2
def check_errors(input):
    indexes = [index for index, row in enumerate(input) if row.split(' ')[0] == 'jmp' or row.split(' ')[0] == 'nop']
    for index in indexes:
        temp_input = change_operation(input.copy(), index)
        if(run(temp_input) == True):
            return


def change_operation(input, index):
    instruction = input[index]
    cur_type, val = instruction.split(' ')
    if(cur_type == 'jmp'):
        input[index] = 'nop ' + val
    else:
        input[index] = 'jmp ' + val
    return input


# RUN 
starttime = time.time()
run(input)
check_errors(input)
endtime = time.time()
print("Total execution time:", endtime - starttime)