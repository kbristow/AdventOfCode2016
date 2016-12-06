def is_a_real_room(name, expected_hash):
    letter_counts = {}
    for letter in name:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    sorted_letter_counts = []
    for letter in letter_counts:
        new_entry = (letter, letter_counts[letter])
        if len(sorted_letter_counts) == 0:
            sorted_letter_counts += [new_entry]
        else:
            inserted = False
            for i in range(0, len(sorted_letter_counts)):
                if sorted_letter_counts[i][1] < letter_counts[letter] or \
                        (sorted_letter_counts[i][1] == letter_counts[letter] and sorted_letter_counts[i][0] > letter):
                    sorted_letter_counts.insert(i, new_entry)
                    inserted = True
                    break
            if not inserted:
                sorted_letter_counts += [new_entry]
    required_hash = ""
    for i in range(0, min(len(sorted_letter_counts), 5)):
        required_hash += sorted_letter_counts[i][0]

    return required_hash == expected_hash


with open("a.in") as file_handle:
    lines = file_handle.readlines()

total_id_sum = 0
for line in lines:
    line = line.strip()
    line_split = line.split("-")
    encrypted_name = "".join(line_split[:-1])
    sector_id = line_split[-1].split("[")[0]
    hash_code = line_split[-1].split("[")[1][:-1]
    if is_a_real_room(encrypted_name, hash_code):
        total_id_sum += int(sector_id)

print "The total sector id sum is: " + str(total_id_sum)