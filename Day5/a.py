import hashlib


def find_password(door_id):
    """ Feel like there must be a better way to do this """
    code = ""
    count = 0
    while len(code) < 8:
        md5 = hashlib.md5(door_id + str(count)).hexdigest()
        if md5.startswith("00000"):
            code += md5[5]
        count += 1
    return code

with open("a.in") as file_handle:
    line = file_handle.read().strip()

print find_password(line)
