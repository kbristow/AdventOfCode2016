def find_first_duplicate_location(instructions):
    current_direction = 0
    distances = [0, 0]
    visited_locations = [(0, 0)]

    for instruction in instructions:
        instruction = instruction.strip()
        if instruction[0] == 'R':
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction + 3) % 4
        multiplier = 1 if current_direction < 2 else -1
        for i in range(0, int(instruction[1:])):
            distances[current_direction % 2] += multiplier
            location = (distances[0], distances[1])
            if location in visited_locations:
                return location
            else:
                visited_locations += [location]
    return None

with open("b.in") as file_handle:
    line = file_handle.readline()

position = find_first_duplicate_location(line.split(','))
print "Distance to HQ: " + str(abs(position[0]) + abs(position[1]))
