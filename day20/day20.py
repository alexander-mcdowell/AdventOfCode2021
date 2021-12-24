##########
# PART 1 #
##########

# This should not have taken as long as it did for me to solve part 1...
# All I had to do was change the symbol I was padding with.

"""
data = open("day20in.txt").read().split("\n")
algorithm = data[0]
# Empty line at data[1]
grid = [[(1 if data[i][j] == '#' else 0) for j in range(len(data[i]))] for i in range(2, len(data))]

def print_g(grid):
    for x in grid:
        for y in x:
            print("#" if y == 1 else ".", end = "")
        print()

def expand(grid, algorithm, fill):
    n = len(grid) + 4
    m = len(grid[0]) + 4
    
    expanded = [[0 for _ in range(len(grid[0]) + 2)] for _ in range(len(grid) + 2)]
    padded = []
    for i in range(n):
        padded.append([])
        
        for j in range(m):
            i_g, j_g = i - 2, j - 2
            if (i_g >= 0 and i_g < len(grid) and j_g >= 0 and j_g < len(grid[0])): padded[-1].append(grid[i_g][j_g])
            else: padded[-1].append(int(fill == '#'))
    
    for i in range(2, n):
        for j in range(2, m):
            window = ""
            for ki in [-2, -1, 0]:
                for kj in [-2, -1, 0]:
                    window += str(padded[i + ki][j + kj])

            decimal = int(window, 2)
            expanded[i - 2][j - 2] = int(algorithm[decimal] == '#')

    return expanded

fill = '.'
for _ in range(2):
    grid = expand(grid, algorithm, fill)
    fill = algorithm[int("".join([str(int(fill == '#'))] * 9), 2)]

count = 0
for x in grid: count += sum(x)
print(count)
"""

##########
# PART 2 #
##########

# Easy change from Part 1. Just change 2 to 50.

data = open("day20in.txt").read().split("\n")
algorithm = data[0]
# Empty line at data[1]
grid = [[(1 if data[i][j] == '#' else 0) for j in range(len(data[i]))] for i in range(2, len(data))]

def print_g(grid):
    for x in grid:
        for y in x:
            print("#" if y == 1 else ".", end = "")
        print()

def expand(grid, algorithm, fill):
    n = len(grid) + 4
    m = len(grid[0]) + 4
    
    expanded = [[0 for _ in range(len(grid[0]) + 2)] for _ in range(len(grid) + 2)]
    padded = []
    for i in range(n):
        padded.append([])
        
        for j in range(m):
            i_g, j_g = i - 2, j - 2
            if (i_g >= 0 and i_g < len(grid) and j_g >= 0 and j_g < len(grid[0])): padded[-1].append(grid[i_g][j_g])
            else: padded[-1].append(int(fill == '#'))
    
    for i in range(2, n):
        for j in range(2, m):
            window = ""
            for ki in [-2, -1, 0]:
                for kj in [-2, -1, 0]:
                    window += str(padded[i + ki][j + kj])

            decimal = int(window, 2)
            expanded[i - 2][j - 2] = int(algorithm[decimal] == '#')

    return expanded

fill = '.'
for _ in range(50):
    grid = expand(grid, algorithm, fill)
    fill = algorithm[int("".join([str(int(fill == '#'))] * 9), 2)]

count = 0
for x in grid: count += sum(x)
print(count)