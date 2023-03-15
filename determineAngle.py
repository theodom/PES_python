from simpelModel import create_bounce
import math
import numpy as np



"""
    @param v_0: starting velocity of the projectile ()
    @param x_target: straight line distance to target, 12 m by default
    @param y_target: height of the target, 0.3 m by default
    
    @return best_angle: most optimal launch angle for input parameters (in degrees)
"""
def optimize(v_0,x_target = 12, y_target = 0.3):
    possible_thetas = dict()
    for i in range(360):
        theta = float(i/8)
        x,y = create_bounce(v_0,theta)
        distance = determine_distance(x,y,x_target,y_target)
        possible_thetas[theta] = abs(distance)
    
    best_angle = min(possible_thetas, key= lambda k: possible_thetas[k])
    
    
    print("best angle: ",best_angle)
    print("distance: ",possible_thetas[best_angle])
    while len(possible_thetas) > 10:
        possible_thetas.pop(max(possible_thetas, key= lambda k: possible_thetas[k]))
    
    print("10 best closest: ",possible_thetas)
    return best_angle


def determine_distance(x,y,x_target,y_target):

    t = np.linspace(0,10,1000)
    y_reverse = y[::-1]
    index = 0
    for i in range(len(t)):
        if y_reverse[i] - 0.015 < y_target and y_reverse[i] + 0.015 > y_target:
            index = i
            break
    x_hit = x[len(t)-index-1]

    return x_target - x_hit