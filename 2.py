#!/bin/env python

# 2. Find the bathroom keycode

# Input is a series of U, D, L, R instructions for up, down, left or right

# The gameboard is a 3x3 grid from 1-9 (a numpad with 1 at 0,0 in top left)

# Starting from the last point reached ("5" to start), follow each move
# instruction (ignoring those that would move you off the edge of the pad)
# until a final point is reached and record the number for that point.

# Find all numbers to get the combination to unlock the door.

import sys

with open('2.input', 'rb') as fh:
    data = fh.readlines()

# Part 1
pad = ((1, 2, 3),
       (4, 5, 6),
       (7, 8, 9))

# Solution one: perform bounds checking for every movement...not good.
# could prolly do some type of matrix transposition with numpy or such.
# but i'll just use another lookup table (did i mention i like those?).
# see solution 2 below
point = (1,1) # start at 5
for line in data:
    for instruction in line.strip():
        if instruction == 'U':
            y = point[1] - 1
            if y >= 0:
                point = (point[0], y)
        elif instruction == 'D':
            y = point[1] + 1
            if y < 3:
                point = (point[0], y)
        elif instruction == 'L':
            x = point[0] - 1
            if x >= 0:
                point = (x, point[1])
        elif instruction == 'R':
            x = point[0] + 1
            if x < 3:
                point = (x, point[1])
    sys.stdout.write(str(pad[point[1]][point[0]]))
sys.stdout.write('\n')


# Solution two: precumpute a map of legal movements

# pulled the loop from the second solution to part one into a function
# since it turns out part two can use it as well
def calculate_keycode(data, point, pad, pad_map):
    code = []
    for line in data:
        for instruction in line.strip():
            number = pad[point[1]][point[0]]
            if instruction in ('U', 'D'):
                point = (point[0], point[1] + pad_map[instruction][number])
            if instruction in ('L', 'R'):
                point = (point[0] + pad_map[instruction][number], point[1])
        code.append(str(pad[point[1]][point[0]]))
    return ''.join(code)


pad = ((1, 2, 3),
       (4, 5, 6),
       (7, 8, 9))
number = 5
point = (1, 1) # start at 5
# yeah, did i menation that lookup tables are the shit and are
# under-untilized in python and ruby?
pad_map = {
    'U': {1: 0, 2: 0, 3: 0, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1, 9: -1},
    'L': {1: 0, 2: -1, 3: -1, 4: 0, 5: -1, 6: -1, 7: 0, 8: -1, 9: -1},
    'D': {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0},
    'R': {1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 0, 7: 1, 8: 1, 9: 0}
}
print(calculate_keycode(data, point, pad, pad_map))


# Part 2 - the bobs installed a new numpad...fooking bobs
pad = ((0, 0, 1, 0, 0),
       (0, 2, 3, 4, 0),
       (5, 6, 7, 8, 9),
       (0, 'A', 'B', 'C', 0),
       (0, 0, 'D', 0, 0))
point = (0, 2) # start at 5
# hey look...another lookup table!
pad_map = {
    'U': {1: 0, 2: 0, 3: -1, 4: 0, 5: 0, 6: -1, 7: -1, 8: -1, 9: 0, 'A': -1, 'B': -1, 'C': -1, 'D': -1},
    'L': {1: 0, 2: 0, 3: -1, 4: -1, 5: 0, 6: -1, 7: -1, 8: -1, 9: -1, 'A': 0, 'B': -1, 'C': -1, 'D': 0},
    'D': {1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 7: 1, 8: 1, 9: 0, 'A': 0, 'B': 1, 'C': 0, 'D': 0},
    'R': {1: 0, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 7: 1, 8: 1, 9: 0, 'A': 1, 'B': 1, 'C': 0, 'D': 0}
}
print(calculate_keycode(data, point, pad, pad_map))
