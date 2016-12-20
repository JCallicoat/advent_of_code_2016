#!/bin/env python

# 6

# Part one

# In this model, the same message is sent repeatedly. You've recorded the
# repeating message signal (your puzzle input), but the data seems quite corrupted -
# almost too badly to recover. Almost.
#
# All you need to do is figure out which character is most frequent for each position.
# For example, suppose you had recorded the following messages:
#
# eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar
#
# The most common character in the first column is e; in the second, a;
# in the third, s, and so on. Combining these characters returns the
# error-corrected message, easter.

# Given the recording in your puzzle input, what is the error-corrected version
# of the message being sent?

import string

with open('6.input', 'rb') as fh:
    data = [line.strip() for line in fh.readlines()]

def get_msg(func):
    msg = ''
    for column in zip(*data):
        char_counts = {}
        for char in string.ascii_lowercase:
            char_counts[char] = column.count(char)
        msg += func(char_counts, key=char_counts.get)
    return msg

print(get_msg(max))


# Part 2

# In this modified code, the sender instead transmits what looks like random data,
# but for each character, the character they actually want to send is slightly less
# likely than the others. Even after signal-jamming noise, you can look at the
# letter distributions in each column and choose the least common letter to
# reconstruct the original message.

# In the above example, the least common character in the first column is a;
# in the second, d, and so on. Repeating this process for the remaining characters
# produces the original message, advent.

# Given the recording in your puzzle input and this new decoding methodology,
# what is the original message that Santa is trying to send?

print(get_msg(min))
