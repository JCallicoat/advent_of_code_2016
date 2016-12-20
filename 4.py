#!/bin/env python

# 4

# Part one:

# Each room consists of an encrypted name (lowercase letters separated by dashes)
# followed by a dash, a sector ID, and a checksum in square brackets.
#
# A room is real (not a decoy) if the checksum is the five most common letters
# in the encrypted name, in order, with ties broken by alphabetization. For example:
#
#  aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are
# a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
#
#  a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are
# all tied (1 of each), the first five are listed alphabetically.
#
#  not-a-real-room-404[oarel] is a real room.
#
#  totally-real-room-200[decoy] is not.
#
# Of the real rooms from the list above, the sum of their sector IDs is 1514.
#
# What is the sum of the sector IDs of the real rooms?

import string
from collections import OrderedDict

with open('4.input', 'rb') as fh:
    data = [line.strip() for line in fh.readlines()]

rooms = {}
sector_sum = 0
for line in data:
    name, sector_and_chksum = line.rsplit('-', 1)
    sector = int(sector_and_chksum[:3])
    chksum = sector_and_chksum[4:-1]

    char_counts = OrderedDict()
    for char in string.ascii_lowercase:
        char_counts[char] = name.count(char)

    top_five = ''
    for _ in xrange(5):
        highest = max(char_counts, key=char_counts.get)
        top_five += highest
        del char_counts[highest]

    if top_five == chksum:
        sector_sum += sector
        rooms[name] = sector

print(sector_sum)


# Part 2

# To decrypt a room name, rotate each letter forward through the alphabet a
# number of times equal to the room's sector ID. A becomes B, B becomes C,
# Z becomes A, and so on. Dashes become spaces.
#
# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
#
# What is the sector ID of the room where North Pole objects are stored?

for name, sector in rooms.iteritems():
    name = list(name.replace('-', ' '))
    chars = string.ascii_lowercase * 2
    for i in xrange(len(name)):
        if name[i] == ' ':
            continue
        rotations = sector % len(string.ascii_lowercase)
        index = string.ascii_lowercase.index(name[i])
        name[i] = chars[rotations + index]
    name = ''.join(name)
    if 'northpole' in name:
        print(sector)
