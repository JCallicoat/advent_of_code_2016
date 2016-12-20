#!/bin/env python

# 7

# Part one

# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
# An ABBA is any four-character sequence which consists of a pair of two different
# characters followed by the reverse of that pair, such as xyyx or abba. However,
# the IP also must not have an ABBA within any hypernet sequences, which are
# contained by square brackets.
#
# For example:
#  abba[mnop]qrst supports TLS (abba outside square brackets).
#
#  abcd[bddb]xyyx does not support TLS (bddb is within square brackets,
#  even though xyyx is outside square brackets).
#
#  aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters
#  must be different).
#
#  ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets,
#  even though it's within a larger string).
#
# How many IPs in your puzzle input support TLS?

import string
from itertools import product

with open('7.input', 'rb') as fh:
    data = [line.strip() for line in fh.readlines()]

def check_abbas(to_check):
    for abba in abbas:
        for haystack in to_check:
            if abba in haystack:
                return True

def parse_line(line):
    ips = []
    hypernetz = []
    ip_rest, rest = line.split('[', 1)
    ips.append(ip_rest)
    while ']' in rest:
        hnetz, rest = rest.split(']', 1)
        hypernetz.append(hnetz)
        try:
            ip_rest, rest = rest.split('[', 1)
            ips.append(ip_rest)
        except:
            ips.append(rest)
    return ips, hypernetz

abbas = []
words = [''.join(chars) for chars in
         product(string.ascii_lowercase, repeat=4)]
for word in words:
    if word[0] == word[3] != word[1] and word[1] == word[2]:
        abbas.append(word)

tlsips = []
for line in data:
    # i wasted way too much time here with false positives because i was parsing
    # ip data and hypernet data into two composite strings and some ABBAs formed
    # across the boundries of the different ip segments. >:(
    # they could have made clearer that they were only looking for ABBAs in
    # individual segments and across not the whole IP - like they could have
    # mentioned the "anywhere in the supernet sequences" from the part two
    # instructions in the part one instructions </rant>
    ips, hypernetz = parse_line(line)
    if check_abbas(hypernetz):
        continue
    if check_abbas(ips):
        tlsips.append(line)

print(len(tlsips))


# Part two

# You would also like to know which IPs support SSL (super-secret listening).
#
# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in
# the supernet sequences (outside any square bracketed sections), and a
# corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences.

# An ABA is any three-character sequence which consists of the same character twice
# with a different character between them, such as xyx or aba. A corresponding BAB
# is the same characters but in reversed positions: yxy and bab, respectively.
#
# For example:
#
#  aba[bab]xyz supports SSL (aba outside square brackets with corresponding
#  bab within square brackets).
#
#  xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
#
#  aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet;
#  the aaa sequence is not related, because the interior character must be different).
#
#  zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a
# corresponding bzb, even though zaz and zbz overlap).

# How many IPs in your puzzle input support SSL?

abas = []
words = [''.join(chars) for chars in
         product(string.ascii_lowercase, repeat=3)]
for word in words:
    if word[0] == word[2] != word[1]:
        abas.append(word)

sslips = []
for line in data:
    ips, hypernetz = parse_line(line)
    for ip in ips:
        for aba in abas:
            found = 0
            if aba in ip:
                bab = aba[1] + aba[0] + aba[1]
                for hnet in hypernetz:
                    if bab in hnet:
                        found = 1
                if found:
                    sslips.append(line)
                    break


print(len(sslips))
