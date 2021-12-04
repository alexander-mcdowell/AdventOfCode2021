##########
# PART 1 #
##########

"""
forward = 0
depth = 0
instructions = open("day2in.txt").read().split("\n")
for instruction in instructions:
    if (instruction == ""): break
    command, num = instruction.split(" ")
    num = int(num)
    if (command == "forward"): forward += num
    elif (command == "up"): depth -= num
    elif (command == "down"): depth += num
print(forward * depth)
"""

##########
# PART 2 #
##########

forward = 0
depth = 0
aim = 0
instructions = open("day2in.txt").read().split("\n")
for instruction in instructions:
    if (instruction == ""): break
    command, num = instruction.split(" ")
    num = int(num)
    if (command == "forward"):
        forward += num
        depth += aim * num
    elif (command == "up"): aim -= num
    elif (command == "down"): aim += num
print(forward * depth)