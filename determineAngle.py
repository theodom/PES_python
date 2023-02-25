from schuineWorp import create_bounce, create_plot
import math
from scipy.optimize import newton
import scipy.optimize as spo
import numpy as np


def distance_to_hit_target(v0,theta,x_target,y_target):
    
    x, y = create_bounce(v0,theta)
    x_hit = 0
    prev_hit = 0
    t = np.linspace(0,10,500)
    for i in range(len(t)):
        
        if y_target - 0.02 < y[i] and y[i] < y_target + 0.02:
            prev_hit = x_hit
            x_hit = x[i]
        if x_hit > x_target: 
            x_hit = prev_hit
            break
    
    return x_target - x_hit

def optimise_angle(v0,x_target,y_target):
    
    for i in range(0,360):
        theta = i/4
        distance = distance_to_hit_target(v0,theta,x_target,y_target)
        if abs(distance) < 0.02:
            return theta
    return None



#bronvermelding spo.minimize: https://www.youtube.com/watch?v=G0yP_TM-oag