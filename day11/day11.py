##########
# PART 1 #
##########

"""
data = open("day11in.txt").read().split("\n")
grid = [[int(c) for c in line] for line in data]
n = len(grid)

num_flashes = 0
N = 100
for _ in range(N):
    flash_matrix = [[False for _ in range(n)] for _ in range(n)]
    queue = []
    for i in range(n):
        for j in range(n):
            grid[i][j] += 1
            if (grid[i][j] > 9):
                queue.append((i, j))
    
    while len(queue) != 0:
        i, j = queue.pop(0)
        if (i < 0 or j < 0 or i > n - 1 or j > n - 1): continue
        if (flash_matrix[i][j]): continue
        
        if (grid[i][j] >= 9):
            grid[i][j] = 0
            flash_matrix[i][j] = True
            num_flashes += 1
            
            for k_i in [-1, 0, 1]:
                for k_j in [-1, 0, 1]:
                    if (k_i == 0 and k_j == 0): continue
                    queue.append((i + k_i, j + k_j))
        else:
            grid[i][j] += 1

print(num_flashes)
"""

##########
# PART 2 #
##########

data = open("day11in.txt").read().split("\n")
grid = [[int(c) for c in line] for line in data]
n = len(grid)
step_num = 1

while (True):
    num_flashes = 0
    flash_matrix = [[False for _ in range(n)] for _ in range(n)]
    queue = []
    for i in range(n):
        for j in range(n):
            grid[i][j] += 1
            if (grid[i][j] > 9):
                queue.append((i, j))
    
    while len(queue) != 0:
        i, j = queue.pop(0)
        if (i < 0 or j < 0 or i > n - 1 or j > n - 1): continue
        if (flash_matrix[i][j]): continue
        
        if (grid[i][j] >= 9):
            grid[i][j] = 0
            flash_matrix[i][j] = True
            num_flashes += 1
            
            for k_i in [-1, 0, 1]:
                for k_j in [-1, 0, 1]:
                    if (k_i == 0 and k_j == 0): continue
                    queue.append((i + k_i, j + k_j))
        else:
            grid[i][j] += 1
    if (num_flashes == n * n):
        print(step_num)
        break
    
    step_num += 1