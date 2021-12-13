##########
# PART 1 #
##########

"""
data = open("day13in.txt").read().split("\n")
N = 1500
grid = [[0 for _ in range(N)] for _ in range(N)]
i = 0
for line in data:
    if (line == ""): break
    x, y = line.split(",")
    x, y = int(x), int(y)
    grid[y][x] = 1
    i += 1

# Fold the grid
M = N
for line in data[i + 1:]:
    axis, val = line.replace("fold along ", "").split("=")
    val = int(val)
    
    if (axis == "x"):
        for i in range(N):
            for j in range(val): grid[i][j] = grid[i][val + (val - j)] or grid[i][j]
            
        grid = [grid[i][:val] for i in range(N)]
    else:
        for i in range(val):
            for j in range(M): grid[i][j] = grid[val + (val - i)][j] or grid[i][j]

        grid = grid[:val]

    N = len(grid)
    M = len(grid[0])
    break

s = 0
for x in grid: s += sum(x)
print(s)
"""

##########
# PART 2 #
##########

data = open("day13in.txt").read().split("\n")
N = 1500
grid = [[0 for _ in range(N)] for _ in range(N)]
i = 0
for line in data:
    if (line == ""): break
    x, y = line.split(",")
    x, y = int(x), int(y)
    grid[y][x] = 1
    i += 1

# Fold the grid
M = N
for line in data[i + 1:]:
    axis, val = line.replace("fold along ", "").split("=")
    val = int(val)
    
    if (axis == "x"):
        for i in range(N):
            for j in range(val): grid[i][j] = grid[i][val + (val - j)] or grid[i][j]
            
        grid = [grid[i][:val] for i in range(N)]
    else:
        for i in range(val):
            for j in range(M): grid[i][j] = grid[val + (val - i)][j] or grid[i][j]

        grid = grid[:val]

    N = len(grid)
    M = len(grid[0])

for x in grid:
    print(x)