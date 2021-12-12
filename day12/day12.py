##########
# PART 1 #
##########

# Rank 372 solution

"""
data = open("day12in.txt").read().split("\n")
graph = {}
for line in data:
    src, dest = line.split("-")
    if src not in graph: graph[src] = []
    graph[src].append(dest)
    if dest not in graph: graph[dest] = []
    graph[dest].append(src)
    
def recurse_paths(root, path):
    global graph, paths
    new_path = path + [root]
    if (root == "end"):
        paths.append(new_path)
        return
    for dest in graph[root]:
        if (str.islower(dest) and dest in new_path): continue
        recurse_paths(dest, new_path)

paths = []
recurse_paths("start", [])
print(len(paths))
"""

##########
# PART 2 #
##########

data = open("day12in.txt").read().split("\n")
graph = {}
for line in data:
    src, dest = line.split("-")
    if src not in graph: graph[src] = []
    graph[src].append(dest)
    if dest not in graph: graph[dest] = []
    graph[dest].append(src)
    
def recurse_paths(root, path, visited_twice):
    global graph, paths
    new_path = path + [root]
    if (root == "end"):
        paths.append(new_path)
        return
    for dest in graph[root]:
        count = new_path.count(dest)
        if ((dest == "start" or dest == "end") and count == 1): continue
        arg = False
        if (str.islower(dest)):
            if (count >= 2): continue
            if (count == 1 and visited_twice): continue
            if (count == 1): arg = True
        recurse_paths(dest, new_path, arg or visited_twice)

paths = []
recurse_paths("start", [], False)
print(len(paths))