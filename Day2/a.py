def process_instruction_line(start_number, instructions):
    start_number -= 1  # convert to base 0
    location = [start_number % 3, int(start_number/3)]
    for direction in instructions:
        if direction == 'U':
            location[1] = max(0, location[1] - 1)
        elif direction == 'D':
            location[1] = min(2, location[1] + 1)
        elif direction == 'L':
            location[0] = max(0, location[0] - 1)
        elif direction == 'R':
            location[0] = min(2, location[0] + 1)

    final_position = location[1] * 3 + location[0] + 1  # add one to return to the base 1 system
    return final_position

with open("a.in") as file_handle:
    lines = file_handle.readlines()

current_position = 5
code = ""
for line in lines:
    line = line.strip()
    current_position = process_instruction_line(current_position, line)
    code += str(current_position)

print "The code is: " + code
