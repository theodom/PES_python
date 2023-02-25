import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#constants
g = 9.81 #zwaarteveldsterkte
m = 0.5
AIR_RESISTANCE = 0.2
BOUNCE_RESTITUTION_COEFFICIENT = 0.82

#ideal constraints are 61.15° / 28° for v0 = 10 m/s

def create_arc(v0, launch_angle):
    t = np.linspace(0, 10, 1000) # time in ms
    launch_angle = math.radians(launch_angle)
    
    vx0 = v0*math.cos(launch_angle)
    vy0 = v0*math.sin(launch_angle)

    x = vx0 * t - AIR_RESISTANCE * t **2
    
    y = vy0 * t - 0.5 * g * t**2
    vy = vy0 - g * t
    
    return [x,y,vy,t]

def create_plot(x,y):
    
    #create_bounce(x,y)
    #teken een nieuwe parabool met beginparams = eindparams vorige parabool
    y_max = np.max(y)
    _,ax = plt.subplots()
    plt.xlim(0,20)
    plt.ylim(0,4)
    plt.xlabel("distance in meters")
    plt.ylabel("height in meters")
    plt.title("ball trajectory")
    rect = patches.Rectangle((12-0.2, 0),0.4,0.3,linewidth=1,edgecolor= 'black',facecolor="none")
    ax.add_patch(rect)
    ax.plot(x,y,color="red")
    plt.show()
    return

def create_bounce(v0,launch_angle):
    x, y, vy, t = create_arc(v0, launch_angle)
    for i in range(len(t)):
        if y[i] < 0.02 and x[i] > 0.02:
            new_vy0 = - BOUNCE_RESTITUTION_COEFFICIENT * vy[i] 
            bounce_time = t[i]
            i_new = i 
            break
    
    y_new = new_vy0 * t - 0.5 * g * t ** 2
    bounce_index = np.where(t == bounce_time)[0][0]
    for i in range(i_new,len(t)):
        y[i] = y_new[i-bounce_index]
    
    return [x, y]



#example code: non-active for imports in other files
#v0 = float(input("begin velocity (m/s): "))
#launch_angle = float(input("launch angle in degrees: ")); launch_angle = math.radians(launch_angle)
#x, y = create_bounce(v0,launch_angle)
#create_plot(x,y)

