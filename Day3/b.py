def can_line_be_triangle(numbers):
    can_be_triangle = True
    for i in range(0, 3):
        if int(numbers[i]) + int(numbers[(i+1) % 3]) <= int(numbers[(i + 2) % 3]):
            can_be_triangle = False
            break
    return can_be_triangle


def count_possible_triangles(configurations):
    tri_count = 0
    for config in configurations:
        if can_line_be_triangle(config):
            tri_count += 1
    return tri_count

with open("b.in") as file_handle:
    lines = file_handle.readlines()

n_triangles = 0
count = 0
triangles = [[], [], []]
for line in lines:
    line_split = line.strip().split()
    triangles[0] += [int(line_split[0])]
    triangles[1] += [int(line_split[1])]
    triangles[2] += [int(line_split[2])]
    if count == 2:
        count = 0
        n_triangles += count_possible_triangles(triangles)
        triangles = [[], [], []]
    else:
        count += 1

print "Number of Triangles: " + str(n_triangles)
