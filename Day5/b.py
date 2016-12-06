import hashlib


def find_password(door_id):
    code = [""] * 8
    count = 0
    characters_needed = 8
    while characters_needed > 0:
        md5 = hashlib.md5(door_id + str(count)).hexdigest()
        if md5.startswith("00000"):
            index = md5[5]
            if index.isdigit():
                index = int(index)
                if index < 8:
                    if code[index] is "":
                        characters_needed -= 1
                        code[index] = md5[6]
                        print "".join(code)
        count += 1
    return "".join(code)

with open("b.in") as file_handle:
    line = file_handle.read().strip()

print "The password is: " + find_password(line)
