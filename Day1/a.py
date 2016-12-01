def find_distance_to_hq(instructions):
    current_direction = 0
    distances = [0, 0]
    for instruction in instructions:
        instruction = instruction.strip()
        if instruction[0] == 'R':
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction + 3) % 4
        multiplier = 1 if current_direction < 2 else -1
        distances[current_direction % 2] += multiplier * int(instruction[1:])
    return distances

with open("a.in") as file_handle:
    line = file_handle.readline()

position = find_distance_to_hq(line.split(','))
print "Distance to HQ: " + str(abs(position[0]) + abs(position[1]))
