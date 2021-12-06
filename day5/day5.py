##########
# PART 1 #
##########
"""
data = open("day5in.txt").read().split("\n")

at_least_two = 0
N = 1000
grid = [[0 for _ in range(N)] for _ in range(N)]
for line in data:
    if (line == ""): break
    src, dest = line.split(" -> ")
    src = src.split(",")
    src = (int(src[0]), int(src[1]))
    dest = dest.split(",")
    dest = (int(dest[0]), int(dest[1]))
    
    # Vertical line
    if (src[0] == dest[0]):
        k = src[1]
        change = -1 if src[1] - dest[1] > 0 else 1
        while (k != dest[1]):
            grid[k][src[0]] += 1
            if (grid[k][src[0]] == 2): at_least_two += 1
            k += change
        grid[k][src[0]] += 1
        if (grid[k][src[0]] == 2): at_least_two += 1
    # Horizontal line
    elif (src[1] == dest[1]):
        k = src[0]
        change = -1 if src[0] - dest[0] > 0 else 1
        while (k != dest[0]):
            grid[src[1]][k] += 1
            if (grid[src[1]][k] == 2): at_least_two += 1
            k += change
        grid[src[1]][k] += 1
        if (grid[src[1]][k] == 2): at_least_two += 1
    # Ignore other lines
    else:
        pass

print(at_least_two)
"""

##########
# PART 2 #
##########

# Part 2 got rank #811 on the global leaderboard.

data = open("day5in.txt").read().split("\n")

at_least_two = 0
N = 1000
grid = [[0 for _ in range(N)] for _ in range(N)]
for line in data:
    if (line == ""): break
    src, dest = line.split(" -> ")
    src = src.split(",")
    src = (int(src[0]), int(src[1]))
    dest = dest.split(",")
    dest = (int(dest[0]), int(dest[1]))
    
    # Vertical line
    if (src[0] == dest[0]):
        k = src[1]
        change = -1 if src[1] - dest[1] > 0 else 1
        while (k != dest[1]):
            grid[k][src[0]] += 1
            if (grid[k][src[0]] == 2): at_least_two += 1
            k += change
        grid[k][src[0]] += 1
        if (grid[k][src[0]] == 2): at_least_two += 1
    # Horizontal line
    elif (src[1] == dest[1]):
        k = src[0]
        change = -1 if src[0] - dest[0] > 0 else 1
        while (k != dest[0]):
            grid[src[1]][k] += 1
            if (grid[src[1]][k] == 2): at_least_two += 1
            k += change
        grid[src[1]][k] += 1
        if (grid[src[1]][k] == 2): at_least_two += 1
    # Diagonal line at 45 degrees
    else:
        k, j = src[0], src[1]
        k_change = -1 if src[0] - dest[0] > 0 else 1
        j_change = -1 if src[1] - dest[1] > 0 else 1
        
        while (k != dest[0]):
            grid[j][k] += 1
            if (grid[j][k] == 2): at_least_two += 1
            j += j_change
            k += k_change
            
        grid[j][k] += 1
        if (grid[j][k] == 2): at_least_two += 1

print(at_least_two)
