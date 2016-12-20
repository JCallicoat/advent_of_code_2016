#!/bin/env python

# 1: Find shortest path from Santa's current location (0,0)N to Easter Bunny HQ.

# Part 1

# Input is a series of movement commands in the form of R<N>, L<N>
# where R or L represent right or left, N represents the number of spaces to move
# in that direction until stopping at the next intersection

# The final point will be the location of the HQ

# Counting using cabdriver geometry, where distance is always counted along one edge
# of a space (never diagonally through it), find the distance of shortest path to
# the HQ from Santa's starting location

hq_location = (-1, -1)
start_location = (0, 0)

visited = [start_location]

location = start_location
orientation = 'N'

orientation_map = {
    'N': {'R': 'E', 'L': 'W'},
    'S': {'R': 'W', 'L': 'E'},
    'E': {'R': 'S', 'L': 'N'},
    'W': {'R': 'N', 'L': 'S'}
}

with open('1.input', 'rb') as fh:
    data = fh.read().strip()

for move_command in data.split(', '):
    direction = move_command[:1]
    distance = int(move_command[1:])

    # this could probably be golfed using modulo 4 for the orientations.
    # i don't want to be that clever, i'll just use a lookup table instead.
    orientation = orientation_map[orientation][direction]

    if orientation == 'N':
        # for use in part 2 below
        # intersections along a path could probably be calculated dynamically
        # from a simple list of end locations, but generating a static list of
        # all visited locations to check against works.
        for i in xrange(1, distance + 1):
            visited.append((location[0], location[1] + i))
        location = (location[0], location[1] + distance)
    elif orientation == 'S':
        for i in xrange(1, distance + 1):
            visited.append((location[0], location[1] - i))
        location = (location[0], location[1] - distance)
    elif orientation == 'E':
        for i in xrange(1, distance + 1):
            visited.append((location[0] + i, location[1]))
        location = (location[0] + distance, location[1])
    elif orientation == 'W':
        for i in xrange(1, distance + 1):
            visited.append((location[0] - i, location[1]))
        location = (location[0] - distance, location[1])

hq_location = visited[-1]
distance = abs(hq_location[0]) + abs(hq_location[1])
print(distance)


# Part 2
# We need to determine if any movement along a path intersects with another
# previous path. remember we're looking for the first location *visited* twice,
# not *stopped at* twice. we have a list of all visited locations so it's easy.
for index, location in enumerate(visited):
    if location in visited[index + 1:]:
        print(abs(location[0]) + abs(location[1]))
        break


# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.gca()
# ax.set_xticks(np.arange(-200,200,1))
# ax.set_yticks(np.arange(-250,250,1))
# plt.plot(*zip(*visited))
# plt.grid()
# plt.show()
