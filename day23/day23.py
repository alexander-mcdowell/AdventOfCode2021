##########
# PART 1 #
##########

# I did this part by hand and still got rank 763...

##########
# PART 2 #
##########

# This is slow but I don't want to fix it.

import time

def copy(x):
    if (type(x) == int): return x
    elif (type(x) == list): return [y for y in x]
    elif (type(x) == dict):
        copy_dict = {}
        for k in x: copy_dict[k] = copy(x[k])
        return copy_dict

data = open("day23in.txt").read().split("\n")[2:-1]
a_stack, b_stack, c_stack, d_stack = [], [], [], []
for i in range(len(data)):
    a_stack.insert(0, (data[i][3], False))
    b_stack.insert(0, (data[i][5], False))
    c_stack.insert(0, (data[i][7], False))
    d_stack.insert(0, (data[i][9], False))

# Add:
  #D#C#B#A#
  #D#B#A#C#
additional = [['D', 'C', 'B', 'A'], ['D', 'B', 'A', 'C']]
for i in range(len(additional)):
    a_stack.insert(1, (additional[i][0], False))
    b_stack.insert(1, (additional[i][1], False))
    c_stack.insert(1, (additional[i][2], False))
    d_stack.insert(1, (additional[i][3], False))

stacks = {'A': a_stack, 'B': b_stack, 'C': c_stack, 'D': d_stack}
cost_map = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
for c in "ABCD":
    for i in range(len(stacks[c]) - 1, -1, -1):
        if (stacks[c][i][0] != c): continue
        flag = True
        for j in range(i - 1, -1, -1):
            if (stacks[c][j][0] != c):
                flag = False
                break
        if (flag): stacks[c][i] = (c, True)

max_size = len(a_stack)
open_space = ['.'] * 11

def balance_stacks(stacks, open_space):
    global max_size

    # Fill in stacks using what is currently in the open space
    total_cost = 0
    while (True):
        moved = False
        for ch in "ABCD":
            if (len(stacks[ch]) != max_size and (stacks[ch] == [] or set(stacks[ch]) == {(ch, True)})):
                cost = cost_map[ch]
                stack_index = 2 + 2 * (ord(ch) - ord('A'))

                # Check left of the stack
                for i in range(stack_index - 1, -1, -1):
                    if (open_space[i] != '.'):
                        # We found something to add to the stack
                        if (open_space[i] == ch):
                            total_cost += cost * (stack_index - i + (max_size - len(stacks[ch])))
                            stacks[ch].append((ch, True))
                            open_space[i] = '.'
                            moved = True
                        else: break

                # Check right of the stack
                for i in range(stack_index + 1, len(open_space)):
                    if (open_space[i] != '.'):
                        # We found something to add to the stack
                        if (open_space[i] == ch):
                            total_cost += cost * (i - stack_index + (max_size - len(stacks[ch])))
                            stacks[ch].append((ch, True))
                            open_space[i] = '.'
                            moved = True
                        else: break
        if (not moved): break
    
    # Check if all stacks have been balanced.
    flag = True
    for c in 'ABCD': flag &= (stacks[c] == [(c, True)] * max_size)
    if (flag): return (total_cost, True)
    
    # Check pop and move from stack possibilities.
    cost_options = []
    for ch in "ABCD":
        if (len(stacks[ch]) != 0):
            # Skip an element on the stack if it is fixed
            if (stacks[ch][-1][1]): continue
            
            depth = max_size - len(stacks[ch])
            stack_index = 2 + 2 * (ord(ch) - ord('A'))
            x, _ = stacks[ch].pop(-1)
            cost = cost_map[x]
            
            # Check all positions left of the stack.
            for i in range(stack_index - 1, -1, -1):
                if (open_space[i] != '.'): break
                # Ignore spots directly above a stack.
                if (i in [2, 4, 6, 8]): continue
                open_space[i] = x
                added_cost = cost * (1 + stack_index - i + depth)
                min_cost, possible_solve = balance_stacks(copy(stacks), copy(open_space))
                if (possible_solve): cost_options.append(added_cost + min_cost)
                open_space[i] = '.'

            # Check all positions right of the stack.
            for i in range(stack_index + 1, len(open_space)):
                if (open_space[i] != '.'): break
                # Ignore spots directly above a stack.
                if (i in [2, 4, 6, 8]): continue
                open_space[i] = x
                added_cost = cost * (1 + i - stack_index + depth)
                min_cost, possible_solve = balance_stacks(copy(stacks), copy(open_space))
                if (possible_solve): cost_options.append(added_cost + min_cost)
                open_space[i] = '.'
            
            # Restore the previous state.
            stacks[ch].append((x, False))

    if (len(cost_options) != 0): total_cost += min(cost_options)
    return (total_cost, len(cost_options) != 0)

start_time = time.time()
print(balance_stacks(stacks, open_space))
print(time.time() - start_time)