##########
# PART 1 #
##########

# Rank 160 solution

data = open("day9in.txt").read().split("\n")
grid = [[int(c) for c in line] for line in data]
minima = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        # Add each adjacent value to this one to an array
        adjacent = []
        if (i > 0): adjacent.append(grid[i - 1][j])
        if (j > 0): adjacent.append(grid[i][j - 1])
        if (i < len(grid) - 1): adjacent.append(grid[i + 1][j])
        if (j < len(grid[0]) - 1): adjacent.append(grid[i][j + 1])
        
        # Assume this is the minimum.
        # If there are elements larger than this, it is not the minimum.
        found = True
        for x in adjacent:
            if (grid[i][j] >= x):
                found = False
                break
        if (found): minima.append(grid[i][j])

print(sum(minima) + len(minima))

##########
# PART 2 #
##########

# Rank 553 solution

data = open("day9in.txt").read().split("\n")
grid = [[int(c) for c in line] for line in data]

# Same minima code from before
minima = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        adjacent = []
        if (i > 0): adjacent.append(grid[i - 1][j])
        if (j > 0): adjacent.append(grid[i][j - 1])
        if (i < len(grid) - 1): adjacent.append(grid[i + 1][j])
        if (j < len(grid[0]) - 1): adjacent.append(grid[i][j + 1])
        
        found = True
        for x in adjacent:
            if (grid[i][j] >= x):
                found = False
                break
        if (found): minima.append((i, j))

basin_grid = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

# Expand function works as follows:
# Set this pair of indices to True, meaning that it is part
# of a basin that has been already visisted.
# If we find a 9 or reach a visited pair of indices, quit the function.
# Otherwise, expand outward from our current index to find other numbers in the basin.
# While we recurse, increment a global "basin_size" variable that represents the size of the
# basin we are currently exploring.
def expand(i, j, grid, basin_grid):
    global basin_size
    if (grid[i][j] == 9 or basin_grid[i][j]): return
    
    basin_grid[i][j] = True
    basin_size += 1
    if (i < len(grid) - 1): expand(i + 1, j, grid, basin_grid)
    if (j < len(grid[0]) - 1): expand(i, j + 1, grid, basin_grid)
    if (i > 0): expand(i - 1, j, grid, basin_grid)
    if (j > 0): expand(i, j - 1, grid, basin_grid)

basin_sizes = []
# Expand outward from each minimum point
for minimum in minima:
    basin_size = 0
    expand(minimum[0], minimum[1], grid, basin_grid)
    basin_sizes.append(basin_size)

# Take the product of the top 3 largest basin sizes
product = 1
for x in sorted(basin_sizes)[-3:]: product *= x
print(product)