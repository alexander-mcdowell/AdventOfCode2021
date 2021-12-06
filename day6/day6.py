##########
# PART 1 #
##########

# Part 1 got rank #409 on the global leaderboard

"""
data = open("day6in.txt").read().split("\n")[0].split(",")
lantern_fish = [int(x) for x in data]
N = 80
for _ in range(N):
    to_add = 0
    for i in range(len(lantern_fish)):
        lantern_fish[i] -= 1
        if (lantern_fish[i] == -1):
            lantern_fish[i] = 6
            to_add += 1
    lantern_fish += [8] * to_add
print(len(lantern_fish))
"""

##########
# PART 2 #
##########

data = open("day6in.txt").read().split("\n")[0].split(",")
timer = [0] * 9
for x in data: timer[int(x)] += 1
N = 256
for _ in range(N):
    timer.append(timer[0])
    timer.pop(0)
    timer[6] += timer[-1]
print(sum(timer))
