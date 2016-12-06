def rotate_room_name(name, rotations):
    floor = ord('a')
    mod_ceiling = ord('z') - floor + 1

    rotated_name = ""
    for letter in name:
        if letter == " ":
            rotated_name += " "
        else:
            actual_char = chr((ord(letter) - floor + rotations) % mod_ceiling + floor)
            rotated_name += actual_char

    return rotated_name


with open("b.in") as file_handle:
    lines = file_handle.readlines()

for line in lines:
    line = line.strip()
    line_split = line.split("-")
    encrypted_name = " ".join(line_split[:-1])
    sector_id = line_split[-1].split("[")[0]
    decrypted_name = rotate_room_name(encrypted_name, int(sector_id))
    if decrypted_name == "northpole object storage":
        print "Northpole object storage sector id: " + sector_id
        break

