##########
# PART 1 #
##########

"""
data = open("day10in.txt").read().split("\n")
corrupted = 0
for line in data:
    if (line == ""): break
    stack = []
    for c in line:
        if (len(stack) == 0):
            stack.append(c)
            continue
        
        if ((c == ")" and stack[-1] != "(") or
            (c == "}" and stack[-1] != "{") or
            (c == "]" and stack[-1] != "[") or
            (c == ">" and stack[-1] != "<")):
            
            if (c == ")"): corrupted += 3
            elif (c == "]"): corrupted += 57
            elif (c == "}"): corrupted += 1197
            else: corrupted += 25137
            
            break
            
        elif ((c == ")" and stack[-1] == "(") or
            (c == "}" and stack[-1] == "{") or
            (c == "]" and stack[-1] == "[") or
            (c == ">" and stack[-1] == "<")):
            stack.pop(-1)
        else: stack.append(c)

print(corrupted)
"""

##########
# PART 2 #
##########

data = open("day10in.txt").read().split("\n")
scores = []
for line in data:
    if (line == ""): break
    stack = []
    is_corrupted = False
    for c in line:
        if (len(stack) == 0):
            stack.append(c)
            continue
        
        if ((c == ")" and stack[-1] != "(") or
            (c == "}" and stack[-1] != "{") or
            (c == "]" and stack[-1] != "[") or
            (c == ">" and stack[-1] != "<")):
            # Disregard corrupted lines.
            is_corrupted = True
            break
            
        elif ((c == ")" and stack[-1] == "(") or
            (c == "}" and stack[-1] == "{") or
            (c == "]" and stack[-1] == "[") or
            (c == ">" and stack[-1] == "<")):
            stack.pop(-1)
        else: stack.append(c)
    
    if (is_corrupted): continue
    
    # Iterate through the stack backwards.
    score = 0
    while (len(stack) != 0):
        score *= 5
        c = stack.pop(-1)
        if (c == "("): score += 1
        elif (c == "["): score += 2
        elif (c == "{"): score += 3
        else: score += 4
    scores.append(score)

print(sorted(scores)[len(scores)//2])