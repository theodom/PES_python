from schuineWorp import create_bounce
import math
import numpy as np


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