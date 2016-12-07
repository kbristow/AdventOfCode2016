def find_all_aba(literal):
    list_of_aba_in_literal = []
    for i in range(0, len(literal) - 2):
        if literal[i+1] is not literal[i] and literal[i] is literal[i+2]:
            list_of_aba_in_literal += [literal[i:i+3]]
    return list_of_aba_in_literal


def ip_supports_ssl(ip):
    split_left_brackets = ip.split("[")
    list_of_aba = []
    hypernet_literals = []
    for ip_section in split_left_brackets:
        split_right_bracket = ip_section.split("]")
        if len(split_right_bracket) > 1:
            list_of_aba += find_all_aba(split_right_bracket[1])
            hypernet_literals += [split_right_bracket[0]]
        else:
            list_of_aba += find_all_aba(split_right_bracket[0])

    for aba in list_of_aba:
        bab = aba[1] + aba[0] + aba[1]
        for hypernet_literal in hypernet_literals:
            if bab in hypernet_literal:
                return True
    return False


with open("a.in") as file_handle:
    lines = file_handle.readlines()

ssl_ip_count = 0
for line in lines:
    line = line.strip()
    if ip_supports_ssl(line):
        ssl_ip_count += 1


print "Number of IP addresses supporting SSL: " + str(ssl_ip_count)
