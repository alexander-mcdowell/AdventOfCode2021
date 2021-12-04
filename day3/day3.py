##########
# PART 1 #
##########

"""
data = open("day3in.txt").read().split("\n")
gamma, epsilon = "", ""
for i in range(len(data[0])):
    bits = []
    for s in data:
        if (s == ""): break
        bits.append(s[len(s) - i - 1])
    a, b = bits.count("0"), bits.count("1")
    if (a > b):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma = gamma[::-1]
epsilon = epsilon[::-1]
print(int(gamma, 2) * int(epsilon, 2))
"""

##########
# PART 2 #
##########

data = open("day3in.txt").read().split("\n")
oxygen_round, co2_round = data, data
i = 0
while not (len(oxygen_round) == 1 and len(co2_round) == 1):
    # Oxygen rate
    if (len(oxygen_round) != 1):
        zero_s, one_s = [], []
        bits = []
        for s in oxygen_round:
            if (s == ""): break
            if (s[i] == "0"): zero_s.append(s)
            else: one_s.append(s)
            bits.append(s[i])
        a, b = bits.count("0"), bits.count("1")
        
        if (a > b): oxygen_round = zero_s
        else: oxygen_round = one_s
    
    # CO2 rate
    if (len(co2_round) != 1):
        zero_s, one_s = [], []
        bits = []
        for s in co2_round:
            if (s == ""): break
            if (s[i] == "0"): zero_s.append(s)
            else: one_s.append(s)
            bits.append(s[i])
        a, b = bits.count("0"), bits.count("1")
        
        if (a > b): co2_round = one_s
        else: co2_round = zero_s
    
    # Next bit
    i += 1

oxygen = oxygen_round[0]
co2 = co2_round[0]
print(int(oxygen, 2) * int(co2, 2))