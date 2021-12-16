##########
# PART 1 #
##########

"""
hex_string = open("day16in.txt").read().split("\n")[0]
hex_mapper = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
              '4': "0100", '5': "0101", '6': "0110", '7': "0111",
              '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
              'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
bin_string = ""
for c in hex_string: bin_string += hex_mapper[c]

def parse_packets(bin_string):
    if (bin_string == "0" * len(bin_string)): return 0, None
    
    version = int(bin_string[:3], 2)
    type_id = int(bin_string[3:6], 2)

    # Treat as literal
    if (type_id == 4):
        i = 6
        while (True):
            if (bin_string[i] == "0"):
                i += 5
                break
            i += 5
        
        if (i == len(bin_string)): i = None
        return version, i
    else:
        
        # ID = 0: Length of subpackets
        # ID = 1: Number of subpackets
        id = int(bin_string[6])
        if (id == 0): i = 22
        else: i = 18
        
        while (True):
            v, j = parse_packets(bin_string[i:])
            version += v
            if (j == None): break
            i += j
    return version, None

print(parse_packets(bin_string)[0])
"""

##########
# PART 2 #
##########

hex_string = open("day16in.txt").read().split("\n")[0]
hex_mapper = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
              '4': "0100", '5': "0101", '6': "0110", '7': "0111",
              '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
              'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
bin_string = ""
for c in hex_string: bin_string += hex_mapper[c]

def parse_packets(bin_string):
    if (bin_string == "0" * len(bin_string)): return 0, None

    #version = int(bin_string[:3], 2)
    type_id = int(bin_string[3:6], 2)

    # Treat as a literal
    if (type_id == 4):
        i = 6
        s = ""
        while (True):
            s += bin_string[i + 1 : i + 5]
            if (bin_string[i] == "0"):
                i += 5
                break
            i += 5
        
        if (i == len(bin_string)): i = None
        return int(s, 2), i

    id = int(bin_string[6])
    # Length of subpackets
    if (id == 0):
        total_length = int(bin_string[7:22], 2)
        i = 22
    # Number of subpackets
    else:
        num_packets = int(bin_string[7:18], 2)
        i = 18
    
    packet_vals = []
    length_counted = 0
    while (True):
        x, j = parse_packets(bin_string[i:])
        packet_vals.append(x)

        if (j == None): break
        i += j
        length_counted += j
        if (id == 0):
            if (length_counted == total_length): break
        else:
            if (len(packet_vals) == num_packets): break
    
    # Sum packet
    if (type_id == 0): result = sum(packet_vals)
    # Product packet
    elif (type_id == 1):
        result = 1
        for x in packet_vals: result *= x
    # Minimum packet
    elif (type_id == 2): result = min(packet_vals)
    # Maximum packet
    elif (type_id == 3): result = max(packet_vals)
    # Greater than packet
    elif (type_id == 5): result = int(packet_vals[0] > packet_vals[1])
    # Less than packet
    elif (type_id == 6): result = int(packet_vals[0] < packet_vals[1])
    # Equal to packet
    else: result = int(packet_vals[0] == packet_vals[1])

    return result, i

print(parse_packets(bin_string)[0])