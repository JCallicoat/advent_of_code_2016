#/bin/env python

# 3

# Part one: Find the possible triangles
# (where any two sides are greater than the other side)

with open('3.input', 'rb') as fh:
    data = []
    for line in fh.readlines():
        while '  ' in line:
            line = line.replace('  ', ' ')
        data.append(line.strip())

def is_triangle(triangle):
    a, b, c = triangle
    if a + b > c and a + c > b and b + c > a:
        return True

triangles = 0
for line in data:
    if is_triangle(map(int, line.split(' '))):
        triangles += 1
print(triangles)

# Part two: do the same but read by columns
index = 0
triangles = 0
while index < len(data):
    lines = [map(int, line.split(' ')) for line in data[index:index + 3]]
    triangles += map(is_triangle, zip(*lines)).count(True)
    index += 3
print(triangles)
