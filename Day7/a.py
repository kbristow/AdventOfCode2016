def contains_an_abba(literal):
    for i in range(0, len(literal) - 3):
        if literal[i+1] is not literal[i]:
            front = literal[i+1] + literal[i]
            back = literal[i+2:i+4]
            if front == back:
                return True
    return False


def ip_supports_tls(ip):
    split_left_brackets = ip.split("[")
    supernet_contains_abba = False
    hypernet_contains_abba = False
    for ip_section in split_left_brackets:
        split_right_bracket = ip_section.split("]")
        if len(split_right_bracket) > 1:
            supernet_contains_abba |= contains_an_abba(split_right_bracket[0])
            hypernet_contains_abba |= contains_an_abba(split_right_bracket[1])
        else:
            hypernet_contains_abba |= contains_an_abba(split_right_bracket[0])

    return hypernet_contains_abba and not supernet_contains_abba


with open("a.in") as file_handle:
    lines = file_handle.readlines()

tls_ip_count = 0
for line in lines:
    line = line.strip()
    if ip_supports_tls(line):
        tls_ip_count += 1


print "Number of IP addresses supporting TLS: " + str(tls_ip_count)
