##########
# PART 1 #
##########

# Bad code I hate it but it works

data = open("day25in.txt").read().split("\n")
grid = []
for x in data:
    grid.append([])
    for c in x: grid[-1].append(c)

def step(grid):
    grid_copy = []
    for i in range(len(grid)):
        grid_copy.append([])
        for j in range(len(grid[0])): grid_copy[-1].append(grid[i][j])
    moved = False
    
    # East facing first
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == ">"):
                k = (j + 1) % len(grid[i])
                if (grid[i][k] == "."):
                    grid_copy[i][k] = ">"
                    grid_copy[i][j] = "."
                    moved = True

    grid = [[y for y in x] for x in grid_copy]
    
    # South facing next
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == "v"):
                k = (i + 1) % len(grid)
                if (grid[k][j] == "."):
                    grid_copy[k][j] = "v"
                    grid_copy[i][j] = "."
                    moved = True
                    continue

    return grid_copy, moved

i = 1
while (True):
    grid, moved = step(grid)
    if (not moved): break
    i += 1
print(i)

##########
# PART 2 #
##########

# Not a puzzle so there's nothing to show.