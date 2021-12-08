##########
# PART 1 #
##########

"""
input = open("day8in.txt").read().split("\n")
data = []
count = 0
for line in input:
    if (line == ""): break
    split = line.split(" | ")
    data.append((split[0].split(" "), split[1].split(" ")))
    
    # 1 has two segments
    # 4 has four segments
    # 7 has three segments
    # 8 has seven segments
    for x in data[-1][1]:
        if (len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7): count += 1
print(count)
"""

##########
# PART 2 #
##########

data = open("day8in.txt").read().split("\n")
total = 0
for line in data:
    if (line == ""): break
    
    decode_map = {}
    
    input, output = line.split(" | ")
    input = input.split(" ")
    output = output.split(" ")
    
    d = {}
    for x in input:
        try: d[len(x)].append(x)
        except Exception as _: d[len(x)] = [x]
    input = [d[x] for x in sorted(d)]
    
    # There is only one number of length two: 1.
    decode_map["".join(sorted(input[0][0]))] = 1
    # There is only one number of length three: 7
    decode_map["".join(sorted(input[1][0]))] = 7
    # There is only one number of length four: 4
    decode_map["".join(sorted(input[2][0]))] = 4
    
    # There are three numbers with length five: 2, 3, 5
    # 2's unique = [c, e]
    # 3's unique = [c, f]
    # 5's unique = [b, f]
    uniques = [[], [], []]
    for i in range(len(input[3])):
        for c in input[3][i]:
            for j in range(len(input[3])):
                if (i == j): continue
                if (c not in uniques[i] and c not in input[3][j]):
                    uniques[i].append(c)
        uniques[i] = sorted(uniques[i])

    # Identify 3 by finding the string with each character common to one of the other strings.
    three_unique = None
    for i in range(len(uniques)):
        found = True
        for j in range(len(uniques)):
            if (i == j): continue
            if ((uniques[i][0] not in uniques[j]) and (uniques[i][1] not in uniques[j])):
                found = False
                break
        if (found):
            # We found 3
            decode_map["".join(sorted(input[3].pop(i)))] = 3
            three_unique = uniques.pop(i)
            break
    
    # There are three numbers with length five: 0, 6, 9
    # 0's unique = [c, e]
    # 6's unique = [d, e]
    # 9's unique = [c, d]
    # Create a second uniques list for these numbers
    uniques2 = [[], [], []]
    for i in range(len(input[4])):
        for c in input[4][i]:
            for j in range(len(input[4])):
                if (i == j): continue
                if (c not in uniques2[i] and c not in input[4][j]):
                    uniques2[i].append(c)
        uniques2[i] = sorted(uniques2[i])
    
    # We know that 0's unique equals 2's unique, so we can find 0 and 2.
    found = False
    for i in range(len(uniques)):
        for j in range(len(uniques2)):
            if (uniques[i] == uniques2[j]):
                found = True
                break
        if (found):
            # We found 0 and 2
            decode_map["".join(sorted(input[3].pop(i)))] = 2
            decode_map["".join(sorted(input[4].pop(j)))] = 0
            uniques2.pop(j)
            break
    
    # By process of elimination, we now know 5.
    decode_map["".join(sorted(input[3].pop(0)))] = 5
    
    # Find 9 by looking for the one string with one character in common with three.
    if (uniques2[0][0] in three_unique or uniques2[0][1] in three_unique): nine_index = 0
    else: nine_index = 1
    decode_map["".join(sorted(input[4].pop(nine_index)))] = 9
    
    # By process of elimination, we now know 6
    decode_map["".join(sorted(input[4].pop(0)))] = 6
    
    # There is only one number of length 7: 8
    decode_map["".join(sorted(input[5].pop(0)))] = 8
    
    # Now decode the output
    s = ""
    for x in output: s += str(decode_map["".join(sorted(x))])
    total += int(s)
    
print(total)