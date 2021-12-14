##########
# PART 1 #
##########

"""
# Rank 173 solution

data = open("day14in.txt").read().split("\n")
polymer = data[0]
rules = {}

for rule in data[2:]:
    src, insert = rule.split(" -> ")
    rules[src] = src[0] + insert + src[1]

for _ in range(10):
    i = 0
    while (i < len(polymer) - 1):
        if (polymer[i:i+2] in rules):
            polymer = polymer[:i] + rules[polymer[i:i+2]] + polymer[i + 2:]
            i += 2
        else:
            i += 1
counts = [polymer.count(x) for x in set(polymer)]
print(max(counts) - min(counts))
"""

##########
# PART 2 #
##########

data = open("day14in.txt").read().split("\n")
polymer = data[0]
rules = {}
s = polymer

for rule in data[2:]:
    src, insert = rule.split(" -> ")
    rules[src] = src[0] + insert + src[1]
    s += src

char_set = set(s)
pairs = {}
for x in char_set:
    for y in char_set: pairs[x + y] = 0

for i in range(len(polymer) - 1):
    pairs[polymer[i:i+2]] += 1

N = 40
for _ in range(N):
    new_pairs = {x:pairs[x] for x in pairs}
      
    for pair in pairs:
        if (pairs[pair] > 0 and pair in rules):
            count = pairs[pair]
            
            pair1 = rules[pair][:2]
            new_pairs[pair1] += count
            
            pair2 = rules[pair][1:]
            new_pairs[pair2] += count
            
            new_pairs[pair] -= count
            
    pairs = new_pairs

counts = {c:0 for c in char_set}
for pair in pairs:
    counts[pair[0]] += pairs[pair]
    counts[pair[1]] += pairs[pair]
counts = [counts[x] for x in counts]

# Account for double-counting
# One of these answers is correct
maximum, minimum = max(counts), min(counts)
print((maximum - minimum) // 2, (maximum - minimum) // 2 + 1)