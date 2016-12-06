def can_line_be_triangle(numbers):
    can_be_triangle = True
    for i in range(0, 3):
        if int(numbers[i]) + int(numbers[(i+1) % 3]) <= int(numbers[(i + 2) % 3]):
            can_be_triangle = False
            break
    return can_be_triangle

with open("a.in") as file_handle:
    lines = file_handle.readlines()

n_triangles = 0
for line in lines:
    line = line.strip()
    if can_line_be_triangle(line.split()):
        n_triangles += 1

print "Number of Triangles: " + str(n_triangles)
