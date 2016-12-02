def process_instruction_line(start_location, instructions, keypad):
    keypad_dimension = len(keypad)
    current_location = [start_location[0], start_location[1]]
    for direction in instructions:
        test_location = [current_location[0], current_location[1]]
        if direction == 'U':
            test_location[1] = max(0, test_location[1] - 1)
        elif direction == 'D':
            test_location[1] = min(keypad_dimension - 1, test_location[1] + 1)
        elif direction == 'L':
            test_location[0] = max(0, test_location[0] - 1)
        elif direction == 'R':
            test_location[0] = min(keypad_dimension - 1, test_location[0] + 1)

        if keypad[test_location[1]][test_location[0]] is not None:
            current_location[0] = test_location[0]
            current_location[1] = test_location[1]

    return current_location

with open("b.in") as file_handle:
    lines = file_handle.readlines()

current_position = [0, 2]
code = ""
keypad = [
    [None, None, "1", None, None],
    [None, "2", "3", "4", None],
    ["5", "6", "7", "8", "9"],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]
]

for line in lines:
    line = line.strip()
    current_position = process_instruction_line(current_position, line, keypad)
    code += str(keypad[current_position[1]][current_position[0]])

print "The code is: " + code
