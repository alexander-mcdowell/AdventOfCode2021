inc = -1
last_x = 0
nums = open("day1in.txt").read().split("\n")
for i in range(len(nums) - 2):
    if (nums[i + 2] == ''): break
    x = int(nums[i]) + int(nums[i + 1]) + int(nums[i + 2])
    if (x > last_x): inc += 1
    last_x = x
print(inc)