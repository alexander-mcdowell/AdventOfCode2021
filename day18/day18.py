##########
# PART 1 #
##########

"""
class Node:
    def __init__(self, val, parent, left, right):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

def to_tree(x, parent):
    if (type(x) == int): parent.val = int(x)
    else:
        parent.left = Node(None, parent, None, None)
        to_tree(x[0], parent.left)
        parent.right = Node(None, parent, None, None)
        to_tree(x[1], parent.right)

def check_explode(root, depth):
    # Check if we need to explode this pair
    if (depth == 4 and (root.left != None and root.left.val != None) and (root.right != None and root.right.val != None)):
        #print("Explode " + str([root.left.val, root.right.val]))
        
        # Find the closest node left and add left_add to it
        prev = root
        iter = root.parent
        while (iter != None and (iter.left == prev or iter.left == None)):
            prev = iter
            iter = iter.parent
        if (iter != None):
            iter = iter.left
            while (iter.right != None): iter = iter.right
            #print("Left: ", iter.val, root.left.val)
            iter.val += root.left.val
        
        # Find the closest node right and add right_add to it
        prev = root
        iter = root.parent
        d = depth - 1
        while (iter != None and (iter.right == prev or iter.right == None)):
            prev = iter
            iter = iter.parent
            d -= 1
        if (iter != None):
            iter = iter.right
            d += 1
            while (iter.left != None):
                iter = iter.left
                d += 1
            #print("Right: ", iter.val, root.right.val)
            iter.val += root.right.val
        
        if (root.parent.left == root): root.parent.left = Node(0, root.parent, None, None)
        else: root.parent.right = Node(0, root.parent, None, None)
        
        return True

    # Search left nodes
    if (root.left != None):
        if (check_explode(root.left, depth + 1)): return True
    # Search right nodes
    if (root.right != None):
        if (check_explode(root.right, depth + 1)): return True

    return False

def check_split(root, depth):
    # Split this node if it is a regular number equal to or larger than 10
    if (root.left == None and root.right == None and root.val >= 10):
        #print("Split " + str(root.val))
        
        new_root = Node(None, root.parent, None, None)
        left_val = root.val // 2
        left_n = Node(left_val, new_root, None, None)
        new_root.left = left_n
        right_val = root.val - left_val
        right_n = Node(right_val, new_root, None, None)
        new_root.right = right_n
        
        if (root == root.parent.left): root.parent.left = new_root
        else: root.parent.right = new_root
        
        return True

    # Search left nodes
    if (root.left != None):
        if (check_split(root.left, depth + 1)): return True
    # Search right nodes
    if (root.right != None):
        if (check_split(root.right, depth + 1)): return True

    return False

def print_tree(root, depth):
    if (root == None): return
    for _ in range(depth): print("-", end = "")
    print("{" + str(root.val) + "}")
    print_tree(root.left, depth + 1)
    print_tree(root.right, depth + 1)

data = open("day18in.txt").read().split("\n")
root = None
for x in data:
    if (root == None):
        root = Node(None, None, None, None)
        to_tree(eval(x), root)
        #print_tree(root, 0)
        #print()
    else:
        sibling = Node(None, None, None, None)
        to_tree(eval(x), sibling)
        #print_tree(sibling, 0)
        #print()
        new_root = Node(None, None, root, sibling)
        sibling.parent = new_root
        root.parent = new_root
        root = new_root
        
    while (check_explode(root, 0) or check_split(root, 0)): pass

#print_tree(root, 0)

def magnitude(root):
    if (root == None): return 0
    if (root.left == None and root.right == None): return root.val
    return 3 * magnitude(root.left) + 2 * magnitude(root.right)

print(magnitude(root))
"""

##########
# PART 2 #
##########

class Node:
    def __init__(self, val, parent, left, right):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

def to_tree(x, parent):
    if (type(x) == int): parent.val = int(x)
    else:
        parent.left = Node(None, parent, None, None)
        to_tree(x[0], parent.left)
        parent.right = Node(None, parent, None, None)
        to_tree(x[1], parent.right)

def check_explode(root, depth):
    # Check if we need to explode this pair
    if (depth == 4 and (root.left != None and root.left.val != None) and (root.right != None and root.right.val != None)):
        
        # Find the closest node left and add left_add to it
        prev = root
        iter = root.parent
        while (iter != None and (iter.left == prev or iter.left == None)):
            prev = iter
            iter = iter.parent
        if (iter != None):
            iter = iter.left
            while (iter.right != None): iter = iter.right
            iter.val += root.left.val
        
        # Find the closest node right and add right_add to it
        prev = root
        iter = root.parent
        d = depth - 1
        while (iter != None and (iter.right == prev or iter.right == None)):
            prev = iter
            iter = iter.parent
            d -= 1
        if (iter != None):
            iter = iter.right
            d += 1
            while (iter.left != None):
                iter = iter.left
                d += 1
            iter.val += root.right.val
        
        if (root.parent.left == root): root.parent.left = Node(0, root.parent, None, None)
        else: root.parent.right = Node(0, root.parent, None, None)
        
        return True

    # Search left nodes
    if (root.left != None):
        if (check_explode(root.left, depth + 1)): return True
    # Search right nodes
    if (root.right != None):
        if (check_explode(root.right, depth + 1)): return True

    return False

def check_split(root, depth):
    # Split this node if it is a regular number equal to or larger than 10
    if (root.left == None and root.right == None and root.val >= 10):
        new_root = Node(None, root.parent, None, None)
        left_val = root.val // 2
        left_n = Node(left_val, new_root, None, None)
        new_root.left = left_n
        right_val = root.val - left_val
        right_n = Node(right_val, new_root, None, None)
        new_root.right = right_n
        
        if (root == root.parent.left): root.parent.left = new_root
        else: root.parent.right = new_root
        
        return True

    # Search left nodes
    if (root.left != None):
        if (check_split(root.left, depth + 1)): return True
    # Search right nodes
    if (root.right != None):
        if (check_split(root.right, depth + 1)): return True

    return False

def magnitude(root):
    if (root == None): return 0
    if (root.left == None and root.right == None): return root.val
    return 3 * magnitude(root.left) + 2 * magnitude(root.right)

def clone_tree(root, parent):
    if (root == None): return root
    copy_root = Node(root.val, parent, None, None)
    if (root.left != None): copy_root.left = clone_tree(root.left, copy_root)
    if (root.right != None): copy_root.right = clone_tree(root.right, copy_root)
    return copy_root

data = open("day18in.txt").read().split("\n")
trees = []
for i in range(len(data)):
    src = Node(None, None, None, None)
    to_tree(eval(data[i]), src)
    trees.append(src)
    
max_magnitude = 0
best = None
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        # x + y case
        child1 = clone_tree(trees[i], None)
        child2 = clone_tree(trees[j], None)
        root = Node(None, None, child1, child2)
        child1.parent = root
        child2.parent = root
        
        while (check_explode(root, 0) or check_split(root, 0)): pass
        
        magn = magnitude(root)
        if (magn > max_magnitude): max_magnitude = magn
            
        # y + x case
        child1 = clone_tree(trees[j], None)
        child2 = clone_tree(trees[i], None)
        root = Node(None, None, child1, child2)
        child1.parent = root
        child2.parent = root
        
        while (check_explode(root, 0) or check_split(root, 0)): pass
        
        magn = magnitude(root)
        if (magn > max_magnitude): max_magnitude = magn

print(max_magnitude)