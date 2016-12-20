#/bin/env python

# 3

# Part one: Find the possible triangles
# (where any two sides are greater than the other side)

with open('3.input', 'rb') as fh:
    data = []
    for line in fh.readlines():
        while '  ' in line:
            line = line.replace('  ', ' ').strip()
        data.append(line)

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True

triangles = 0
for line in data:
    if is_triangle(*map(int, line.split(' '))):
        triangles += 1
print(triangles)

# Part two: do the same but read by columns
index = 0
triangles = 0
while index < len(data):
    lines = data[index:index + 3]
    for i in xrange(3):
        lines[i] = map(int, lines[i].split(' '))
    triangles += map(is_triangle, *zip(*lines)).count(True)
    index += 3
print(triangles)
