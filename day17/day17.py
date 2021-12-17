##########
# PART 1 #
##########

# I hate this code but it works

"""
def sign(x):
    if (x == 0): return 0
    elif (x < 0): return -1
    else: return 1

data = open("day17in.txt").read().split("\n")[0]
xs, ys = data.replace("target area: ", "").split(", ")

x1, x2 = xs.replace("x=", "").split("..")
x1, x2 = int(x1), int(x2)
y1, y2 = ys.replace("y=", "").split("..")
y1, y2 = int(y1), int(y2)

v_bound = 200
iterations = 1000
x_vel_bound, y_vel_bound = v_bound, v_bound

best_height, best_vel = 0, (0, 0)
for xvel in range(-x_vel_bound, x_vel_bound + 1):
    for yvel in range(-y_vel_bound, y_vel_bound + 1):
        max_height = 0
        x, y = 0, 0
        vx, vy = xvel, yvel
        
        in_area = False
        for _ in range(iterations):
            x += vx
            y += vy
            if (y > max_height): max_height = y
            
            if ((y < y1 and vy <= 0) or (x > x2 and vx >= 0)): break
            if ((x1 <= x <= x2) and (y1 <= y <= y2)):
                in_area = True
                break
            
            vx -= sign(vx)
            vy -= 1

        if (in_area):
            if (max_height > best_height):
                best_height = max_height
                best_vel = (xvel, yvel)

print(best_height)
"""

##########
# PART 2 #
##########

def sign(x):
    if (x == 0): return 0
    elif (x < 0): return -1
    else: return 1

data = open("day17in.txt").read().split("\n")[0]
xs, ys = data.replace("target area: ", "").split(", ")

x1, x2 = xs.replace("x=", "").split("..")
x1, x2 = int(x1), int(x2)
y1, y2 = ys.replace("y=", "").split("..")
y1, y2 = int(y1), int(y2)

v_bound = 300
iterations = 3000
x_vel_bound, y_vel_bound = v_bound, v_bound

vels = []
for xvel in range(-x_vel_bound, x_vel_bound + 1):
    for yvel in range(-y_vel_bound, y_vel_bound + 1):
        max_height = 0
        x, y = 0, 0
        vx, vy = xvel, yvel
        
        for _ in range(iterations):
            x += vx
            y += vy
            if (y > max_height): max_height = y
            
            if ((y < y1 and vy <= 0) or (x > x2 and vx >= 0)): break
            if ((x1 <= x <= x2) and (y1 <= y <= y2)):
                vels.append((xvel, yvel))
                break
            
            vx -= sign(vx)
            vy -= 1

print(len(vels))

