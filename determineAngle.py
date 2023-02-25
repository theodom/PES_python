from schuineWorp import create_bounce, create_plot
import math
from scipy.optimize import newton
import scipy.optimize as spo
import numpy as np


def distance_to_hit_target(v0,theta,x_target,y_target):
    
    x, y = create_bounce(v0,theta)
    x_hit = 0
    prev_hit = 0
    t = np.linspace(0,10,1000)
    for i in range(len(t)):
        
        if y_target - 0.02 < y[i] and y[i] < y_target + 0.02:
            prev_hit = x_hit
            x_hit = x[i]
        if x_hit > x_target: 
            #x_hit = prev_hit
            print("hit: ",x_hit)
            break
    
    return x_target - x_hit

def optimise_angle(v0,x_target,y_target, list= None):
    
    for i in range(0,720):
        theta = float(i/8)
        print("theta try: ",theta)
        distance = distance_to_hit_target(v0,theta,x_target,y_target)
        
        if abs(distance) < 0.02:
            if list is not None: list.append(theta)
            return theta
    if list is not None:
        print("list; ",list)
    exit("Cannot launch at the specified speed, exiting program")
    



#te bekijken: spo.minimize: https://www.youtube.com/watch?v=G0yP_TM-oa
# ^ lokaal minimum, evt beter zoeken op globaal minimum
