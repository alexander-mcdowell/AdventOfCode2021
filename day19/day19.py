##########
# PART 1 #
##########

"""
# This code is bad and I hate it but it works well enough and I do not have the willpower
# to improve it any further.

data = open("day19in.txt").read().split("\n")

# First, collect all possible orientations of the scanners.
orientations = []
for xrots in range(4):
    for yrots in range(4):
        for zrots in range(4):
            orientation = (1, 2, 3)
            
            # Rotate about the x-axis
            for _ in range(xrots): orientation = (orientation[0], -orientation[2], orientation[1])
            # Rotate about the y-axis
            for _ in range(yrots): orientation = (-orientation[2], orientation[1], orientation[0])
            # Rotate about the z-axis
            for _ in range(zrots): orientation = (-orientation[1], orientation[0], orientation[2])

            if (orientation not in orientations): orientations.append(orientation)

# Next, collect all of the scanners and the beacons that each scanner sees.
scanner_list = []
scans = None
for line in data:
    if (line == ""): scanner_list.append(scans)
    elif ("scanner" in line): scans = []
    else:
        scans.append([int(x) for x in line.split(",")])

# Helper arrays
offsets = [[None for j in range(len(scanner_list))] for i in range(len(scanner_list))]
oriented = [False for j in range(len(scanner_list))]
oriented[0] = True
queue = [0]
visited = [False for _ in range(len(scanner_list))]
offset_relative_zero = [None for i in range(len(scanner_list))]
offset_relative_zero[0] = [0, 0, 0]

# The general procedure is to go from the zeroth scanner to each of the scanners it can see.
# Then we proceed from each of those scanners to find the next set of visible scanners.
# And so on until all possibly visible scanners have been found.
while (len(queue) != 0):
    n1 = queue.pop(0)
    # Skip scanners that we have already seen.
    if (visited[n1]): continue
    visited[n1] = True
    for n2 in range(len(scanner_list)):
        if (n1 == n2 or visited[n2]): continue
        end = False
        
        # Now calculate the relative offset from one scanner to another
        for i in range(len(scanner_list[n1])):
            for orientation in orientations:
                for j in range(len(scanner_list[n2])):
                    offset = [(-1 if (orientation[k] < 0) else 1) * scanner_list[n2][j][abs(orientation[k]) - 1] - scanner_list[n1][i][k] for k in range(3)]
                    
                    counts = 0
                    for k in range(len(scanner_list[n2])):
                        if (k == j): continue
                        possible = [(-1 if orientation[x] < 0 else 1) * scanner_list[n2][k][abs(orientation[x]) - 1] - offset[x] for x in range(3)]
                        if (possible in scanner_list[n1]): counts += 1

                        # There should be at least 12 beacons that are satisfied by this offset
                        # (11 plus the one used to construct the offset)
                        if (counts == 11):
                            #print((n1, n2), offset, orientation)
                            end = True
                            offsets[n1][n2] = offset
                            
                            # Re-orient
                            if (not oriented[n2]):
                                for j in range(len(scanner_list[n2])):
                                    scanner_list[n2][j] = [(-1 if (orientation[x] < 0) else 1) * scanner_list[n2][j][abs(orientation[x]) - 1] for x in range(3)]
                                oriented[n2] = True

                            offset_relative_zero[n2] = [offset_relative_zero[n1][x] + offsets[n1][n2][x] for x in range(3)]
                            queue.append(n2)
                            break
                    if (end): break
                if (end): break
            if (end): break

print(offset_relative_zero)

all_beacons = []
for n in range(len(scanner_list)):
    for i in range(len(scanner_list[n])):
        if (offset_relative_zero[n] != None):
            beacon = [scanner_list[n][i][k] - offset_relative_zero[n][k] for k in range(3)]
            if (beacon not in all_beacons):
                all_beacons.append(beacon)
print(len(all_beacons))
"""

##########
# PART 2 #
##########

# This code is bad and I hate it but it works well enough and I do not have the willpower
# to improve it any further.

data = open("day19in.txt").read().split("\n")

# First, collect all possible orientations of the scanners.
orientations = []
for xrots in range(4):
    for yrots in range(4):
        for zrots in range(4):
            orientation = (1, 2, 3)
            
            # Rotate about the x-axis
            for _ in range(xrots): orientation = (orientation[0], -orientation[2], orientation[1])
            # Rotate about the y-axis
            for _ in range(yrots): orientation = (-orientation[2], orientation[1], orientation[0])
            # Rotate about the z-axis
            for _ in range(zrots): orientation = (-orientation[1], orientation[0], orientation[2])

            if (orientation not in orientations): orientations.append(orientation)

# Next, collect all of the scanners and the beacons that each scanner sees.
scanner_list = []
scans = None
for line in data:
    if (line == ""): scanner_list.append(scans)
    elif ("scanner" in line): scans = []
    else:
        scans.append([int(x) for x in line.split(",")])

# Helper arrays
offsets = [[None for j in range(len(scanner_list))] for i in range(len(scanner_list))]
oriented = [False for j in range(len(scanner_list))]
oriented[0] = True
queue = [0]
visited = [False for _ in range(len(scanner_list))]
offset_relative_zero = [None for i in range(len(scanner_list))]
offset_relative_zero[0] = [0, 0, 0]

# The general procedure is to go from the zeroth scanner to each of the scanners it can see.
# Then we proceed from each of those scanners to find the next set of visible scanners.
# And so on until all possibly visible scanners have been found.
while (len(queue) != 0):
    n1 = queue.pop(0)
    # Skip scanners that we have already seen.
    if (visited[n1]): continue
    visited[n1] = True
    for n2 in range(len(scanner_list)):
        if (n1 == n2 or visited[n2]): continue
        end = False
        
        # Now calculate the relative offset from one scanner to another
        for i in range(len(scanner_list[n1])):
            for orientation in orientations:
                for j in range(len(scanner_list[n2])):
                    offset = [(-1 if (orientation[k] < 0) else 1) * scanner_list[n2][j][abs(orientation[k]) - 1] - scanner_list[n1][i][k] for k in range(3)]
                    
                    counts = 0
                    for k in range(len(scanner_list[n2])):
                        if (k == j): continue
                        possible = [(-1 if orientation[x] < 0 else 1) * scanner_list[n2][k][abs(orientation[x]) - 1] - offset[x] for x in range(3)]
                        if (possible in scanner_list[n1]): counts += 1

                        # There should be at least 12 beacons that are satisfied by this offset
                        # (11 plus the one used to construct the offset)
                        if (counts == 11):
                            #print((n1, n2), offset, orientation)
                            end = True
                            offsets[n1][n2] = offset
                            
                            # Re-orient
                            if (not oriented[n2]):
                                for j in range(len(scanner_list[n2])):
                                    scanner_list[n2][j] = [(-1 if (orientation[x] < 0) else 1) * scanner_list[n2][j][abs(orientation[x]) - 1] for x in range(3)]
                                oriented[n2] = True

                            offset_relative_zero[n2] = [offset_relative_zero[n1][x] + offsets[n1][n2][x] for x in range(3)]
                            queue.append(n2)
                            break
                    if (end): break
                if (end): break
            if (end): break

max_dist = 0
for n1 in range(len(scanner_list)):
    if (offset_relative_zero[n1] == None): continue
    for n2 in range(len(scanner_list)):
        if (n1 == n2 or offset_relative_zero[n2] == None): continue
        dist = 0
        for k in range(3): dist += abs(offset_relative_zero[n1][k] - offset_relative_zero[n2][k])
        if (dist > max_dist): max_dist = dist
print(max_dist)