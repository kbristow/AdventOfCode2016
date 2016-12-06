import copy


def extract_message(letter_counts):
    message = ""
    for i in range(0, len(letter_counts)):
        max_count = 0
        max_letter = ""
        for letter in letter_counts[i]:
            if letter_counts[i][letter] > max_count:
                max_count = letter_counts[i][letter]
                max_letter = letter
        message += max_letter

    return message


def process_message(message, letter_counts):
    new_results = copy.copy(letter_counts)
    for i in range(0, len(message)):
        letter = message[i]
        if new_results[i] is not None and letter in new_results[i]:
            new_results[i][letter] += 1
        else:
            if new_results[i] is None:
                new_results[i] = {}
            new_results[i][letter] = 1
    return new_results


with open("a.in") as file_handle:
    lines = file_handle.readlines()

current_results = [None]*len(lines[0].strip())
for line in lines:
    line = line.strip()
    current_results = process_message(line, current_results)

print "The message is: " + extract_message(current_results)