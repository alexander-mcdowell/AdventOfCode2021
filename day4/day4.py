##########
# PART 1 #
##########

"""
data = open("day4in.txt").read().split("\n")

# Pre-processing shit
guesses = []
for num in data[0].split(","): guesses.append(int(num))
grids = []
grid = None
grid_add = False
print(guesses)
for line in data[1:]:
    if (line == ""):
        if (grid != None):
            grids.append(grid)
            grid_add = False
        continue
    if (not grid_add):
        grid = []
        grid_add = True
    if (grid_add):
        grid.append([])
        i = 0
        while (i < len(line)):
            grid[-1].append(int(line[i : i + 2]))
            i += 3
grids.append(grid)

# Guessing
N = len(grids[0])
win = False
win_grid = []
last_guess = 0
for guess in guesses:
    if (win): break
    
    for grid in grids:
        if (win): break
        
        # Find the guess in the board
        end_find = False
        for i in range(N):
            if (end_find): break
            for j in range(N):
                if (grid[i][j] == guess):
                    grid[i][j] = -1
                    end_find = True
                    break

        for i in range(N):
            # Get the ith column
            col = []
            for j in range(N): col.append(grid[j][i])
            
            # Check for a win on a row or column
            if (sum(grid[i]) == -N or sum(col) == -N):
                win = True
                win_grid = grid
                last_guess = guess
                break

# Sum of unmarked numbers
s = 0
for i in range(N):
    for j in range(N):
        if (win_grid[i][j] != -1): s += win_grid[i][j]
        
print(win_grid)
print(s, last_guess)
print(s * last_guess)
"""

##########
# PART 2 #
##########

data = open("day4in.txt").read().split("\n")

# Pre-processing shit
guesses = []
for num in data[0].split(","): guesses.append(int(num))
grids = []
grid = None
grid_add = False
for line in data[1:]:
    if (line == ""):
        if (grid != None):
            grids.append(grid)
            grid_add = False
        continue
    if (not grid_add):
        grid = []
        grid_add = True
    if (grid_add):
        grid.append([])
        i = 0
        while (i < len(line)):
            grid[-1].append(int(line[i : i + 2]))
            i += 3
grids.append(grid)

# Guessing
N = len(grids[0])
M = len(grids)
end = False
last_grid = None
last_guess = 0
has_won = [False for _ in range(M)]
for guess in guesses:
    if (end): break
    
    for g in range(M):
        if (has_won[g]): continue
        
        # Find the guess in the board
        end_find = False
        for i in range(N):
            if (end_find): break
            for j in range(N):
                if (grids[g][i][j] == guess):
                    grids[g][i][j] = -1
                    end_find = True
                    break

        for i in range(N):
            # Get the ith column
            col = []
            for j in range(N): col.append(grids[g][j][i])
            
            # Check for a win on a row or column
            if (sum(grids[g][i]) == -N or sum(col) == -N):
                has_won[g] = True
                break
        
        # Check if all boards have won
        temp = True
        for x in has_won: temp = temp and x
        if (temp):
            last_grid = grids[g]
            last_guess = guess
            end = True
            break

# Sum of unmarked numbers
s = 0
for i in range(N):
    for j in range(N):
        if (last_grid[i][j] != -1): s += last_grid[i][j]
        
print(s, last_guess)
print(s * last_guess)