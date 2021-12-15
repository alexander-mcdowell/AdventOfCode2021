##########
# PART 1 #
##########

"""
# Rank 419 solution
# Turns out this doesn't work! You can move in any direction, not just down or right.
# I blame the sample data since the optimal path in the sample data for both parts involved moving down and right.

data = open("day15in.txt").read().split("\n")

grid = [[int(x) for x in line] for line in data]
N, M = len(grid), len(grid[0])
total_risk = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
for j in range(1, M): total_risk[0][j] = grid[0][j] + total_risk[0][j - 1]

for i in range(1, N):
    for j in range(M):
        if (j == 0): total_risk[i][j] = total_risk[i - 1][j] + grid[i][j]
        else: total_risk[i][j] = min(total_risk[i][j - 1], total_risk[i - 1][j]) + grid[i][j]

print(total_risk[N - 1][M - 1])
"""

##########
# PART 2 #
##########

# This solution actually solves parts 1 and 2

data = open("day15in.txt").read().split("\n")

grid = [[int(x) for x in line] for line in data if line != ""]
N, M = len(grid), len(grid[0])

grid_map = [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
big_grid = [[0 for _ in range(5 * M)] for _ in range(5 * N)]

for i in range(5 * N):
    for j in range(5 * M):
        big_grid[i][j] = grid_map[i // N][j // M] + grid[i % N][j % M]
        if (big_grid[i][j] > 9): big_grid[i][j] = 1 + (big_grid[i][j] % 10)

N, M = 5 * N, 5 * M

total_risk = [[0 for _ in range(M)] for _ in range(N)]
counted = [[False for _ in range(M)] for _ in range(N)]
queue = [(0, 0)]

while (len(queue) != 0):
    i, j = queue.pop(0)
    
    if (i > 0):
        x = total_risk[i][j] + big_grid[i - 1][j]
        if (total_risk[i - 1][j] == 0 or total_risk[i - 1][j] > x):
            total_risk[i - 1][j] = x
            queue.append((i - 1, j))
    if (j > 0):
        x = total_risk[i][j] + big_grid[i][j - 1]
        if (total_risk[i][j - 1] == 0 or total_risk[i][j - 1] > x):
            total_risk[i][j - 1] = x
            queue.append((i, j - 1))
    if (i < N - 1):
        x = total_risk[i][j] + big_grid[i + 1][j]
        if (total_risk[i + 1][j] == 0 or total_risk[i + 1][j] > x):
            total_risk[i + 1][j] = x
            queue.append((i + 1, j))
    if (j < M - 1):
        x = total_risk[i][j] + big_grid[i][j + 1]
        if (total_risk[i][j + 1] == 0 or total_risk[i][j + 1] > x):
            total_risk[i][j + 1] = x
            queue.append((i, j + 1))

print(total_risk[-1][-1])