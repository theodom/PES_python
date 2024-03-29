import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#constants
g = 9.81 #zwaarteveldsterkte
AIR_RESISTANCE = 0
BOUNCE_RESTITUTION_COEFFICIENT = 0.59

"""
    @param v0: initial velocity of a the projectile
    @param launch_angle: angle at which the projectile is launched
    
    creates a single parabolic curve for movement of a projectile
    
    @return x, y, vy, t: returns arrays for x movement, y movement, vertical y velocity and linspace t
"""
def create_arc(v0, launch_angle):
    t = np.linspace(0, 10, 1000) # time in 10ms interval 
    launch_angle = math.radians(launch_angle)
    
    #beginsnelheden indelen in x,y componenten
    vx0 = v0*math.cos(launch_angle)
    vy0 = v0*math.sin(launch_angle)

    #vergelijkingen x(t) en y(t) (1D np arrays)
    x = vx0 * t - 0.5 * AIR_RESISTANCE * t **2
    y = vy0 * t - 0.5 * g * t**2
    
    vx = vx0 - AIR_RESISTANCE * t
    vy = vy0 - g * t
    
    return [x,y,vx,vy,t]


"""
    @param v0: initial velocity of a the projectile
    @param launch_angle: the angle at which the projectile is launched
    
    creates the full trajectory of a projectile with bounce
    
    @return x, y: returns arrays for x position, y position in function of t (linspace representing time)
"""
def create_bounce(v0,launch_angle):
    new_vy0 = None
    x, y, vx, vy, t = create_arc(v0, launch_angle)
    for i in range(len(t)):
        if y[i] < 0.02 and x[i] > 0.02:
            new_vy0 = - BOUNCE_RESTITUTION_COEFFICIENT * vy[i] 
            new_vx0 = BOUNCE_RESTITUTION_COEFFICIENT * v0*math.cos(launch_angle)
            bounce_time = t[i]
            i_new = i 
            break
    if new_vy0 is not None:

        y_new = new_vy0 * t - 0.5 * g * t ** 2
        x_new = new_vx0 * t - 0.5 * AIR_RESISTANCE * t **2
        bounce_index = np.where(t == bounce_time)[0][0]
        for i in range(i_new,len(t)):
            y[i] = max(0,y_new[i-bounce_index])
    #print(x)
    return [x, y]


"""
    @param x: 1D array with horizontal position
    @param y: 1D array with vertical position
    @param x_guess: compare trajectory with guess, None by default
    @param y_guess: compare trajectory with guess, None by default
    @param x_target: distance of start x to target, 12 by default
    @param y_target: height of target, 0.3 by default
    
    plots the given arrays in an xy-plane
    
    @return
"""
def create_plot(x,y,x_guess = None, y_guess = None, x_target = 12,y_target = 0.3):
    
    y_max = np.max(y) #eventueel gebruikt voor hoogte plot in te stellen, afhankelijk van voorkeur, niet verwijderen
    _,ax = plt.subplots()
    plt.xlim(0,15)
    plt.ylim(0,4.5)
    plt.xlabel("horizontale afstand (m)")
    plt.ylabel("hoogte (m)")
    plt.title("ball trajectory")
    rect = patches.Rectangle((x_target-0.1, 0),0.2,y_target,linewidth=1,edgecolor= 'black',facecolor="none")
    ax.add_patch(rect)
    if (type(x_guess) and type(y_guess)) is not None:
        ax.plot(x_guess,y_guess, color="red")
    ax.plot(x,y,color="blue")
    
    plt.show()
    return

#lijst met rechte afstanden tot middelpunt van de emmer
def get_emmers():
    lijst = dict()
    lijst[0] = 11.4035
    lijst[1] = 11.66735
    lijst[2] = lijst[1]
    lijst[3] = 11.875
    lijst[4] = 12.00
    lijst[5] = lijst[3]
    
    return lijst