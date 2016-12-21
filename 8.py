#!/bin/env python

# 8

# Part one

# The magnetic strip on the card you swiped encodes a series of instructions for
# the screen; these instructions are your puzzle input. The screen is 50 pixels
# wide and 6 pixels tall, all of which start off, and is capable of three somewhat
# peculiar operations:
#
#  rect AxB turns on all of the pixels in a rectangle at the top-left of the
#  screen which is A wide and B tall.

#  rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right
#  by B pixels. Pixels that would fall off the right end appear at the left end of the row.

#  rotate column x=A by B shifts all of the pixels in column A (0 is the left column)
#  down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
#
# For example, here is a simple sequence on a smaller screen:
#
#   rect 3x2 creates a small rectangle in the top-left corner:
#
#     ###....
#     ###....
#     .......
#
#   rotate column x=1 by 1 rotates the second column down by one pixel:
#
#     #.#....
#     ###....
#     .#.....
#
#   rotate row y=0 by 4 rotates the top row right by four pixels:
#
#     ....#.#
#     ###....
#     .#.....
#
#   rotate column x=1 by 1 again rotates the second column down by one pixel,
#   causing the bottom pixel to wrap back to the top:
#
#     .#..#.#
#     #.#....
#     .#.....
#
# There seems to be an intermediate check of the voltage used by the display:
# after you swipe your card, if the screen did work, how many pixels should be lit?

with open('8.input', 'rb') as fh:
    data = [line.strip() for line in fh.readlines()]

# yeah i cheesed it...i mean, the first part just wanted the total number lit...
# i had a feeling the second part would ask about the actual content of the screen
# but no point in gold-plating it until it's needed
lit_sum = 0
for line in data:
    if line.startswith('rect '):
        width, height = line[5:].split('x')
        lit_sum += (int(width) * int(height))
print(lit_sum)


# Part the second

# You notice that the screen is only capable of displaying capital letters;
# in the font it uses, each letter is 5 pixels wide and 6 tall.

screen = []
for i in xrange(30):
    screen.append(list('-' * 50))

def print_screen():
    for i, row in enumerate(screen):
        if i < 6:
            print(''.join(row))

def rect(width, height):
    # print('rect', width, height)
    for x in xrange(height):
        for y in xrange(width):
            screen[x][y] = '#'
    # print_screen()

def rotate_col(col, by):
    # print('rotate_col', col, by)
    for i in reversed(range(30)):
        y = i + by
        if y > 30: y -= 30
        if screen[i][col] == '#':
            screen[i][col] = '-'
            screen[y][col] = '#'
    # print_screen()

def rotate_row(row, by):
    # print('rotate_row', row, by)
    new_row = list('-' * 50)
    for i, led in enumerate(screen[row]):
        if led == '#':
            x = i + by
            if x >= 50: x -= 50
            new_row[x] = '#'
    screen[row] = new_row
    # print_screen()

for line in data:
    if line.startswith('rect '):
        rect(*map(int, line[5:].split('x')))
    elif line.startswith('rotate column x='):
        rotate_col(*map(int, line[16:].split(' by ')))
        # rotate_col(0, 33)
        # break
    elif line.startswith('rotate row y='):
        rotate_row(*map(int, line[13:].split(' by ')))

print('')
print_screen()
