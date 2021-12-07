##########
# PART 1 #
##########

# Rank 511
"""
arr = sorted([int(x) for x in open("day7in.txt").read().split("\n")[0].split(",")])
midpoint = arr[len(arr)//2]
s = 0
for x in arr: s += abs(x - midpoint)
print(s)
print(midpoint, sum(arr) / len(arr))
"""

##########
# PART 2 #
##########

# Rank 558

# Shitty version
"""
arr = sorted([int(x) for x in open("day7in.txt").read().split("\n")[0].split(",")])
best_s = 1000000000000000
for compare in range(1, max(arr) + 1):
    s = 0
    for x in arr:
        y = abs(x - compare)
        s += y * (y + 1) // 2
    if (s < best_s): best_s = s
print(best_s)
"""

# Efficient version (I made this after my shitty version worked).
arr = sorted([int(x) for x in open("day7in.txt").read().split("\n")[0].split(",")])
avg = sum(arr)//len(arr)
# The function we are trying to minimize is f(compare) = sum(|arr[i] - n| * (|arr[i] - n| + 1) / 2)
# from i = 0 to i = len(arr) - 1
# If you work out the math, you find that the function is minimized when
# n = average(arr) - (1/(2 * len(arr))) * sum(|arr[i] - n|) from i = 0 to i = len(arr) - 1
# I don't know how to solve this equation further, but I reason that it should be relatively small.
# This is what interval_dist is. The distance away from the average to check for a minimum point.
interval_dist = 15

best_s = 1000000000000000000
for compare in range(max(0, avg - interval_dist), avg + interval_dist + 1):
    s = 0
    for x in arr:
        y = abs(x - compare)
        s += y * (y + 1) // 2
    if (s < best_s):
        best_s = s
    else: break
print(best_s)