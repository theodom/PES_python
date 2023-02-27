from schuineWorp import create_bounce
import math
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
        if abs(x_hit - x_target) < 0.02 : 
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



def optimize(v_0,x_target = 12, y_target = 0.3):
    possible_thetas = dict()
    for i in range(720):
        theta = float(i/8)
        x,y = create_bounce(v_0,theta)
        distance = determine_distance(x,y,x_target,y_target)
        possible_thetas[theta] = abs(distance)
    
    best_angle = min(possible_thetas, key= lambda k: possible_thetas[k])
    print("best angle: ",best_angle)
    print("distance: ",possible_thetas[best_angle])
    #print("angles: ",possible_thetas)


    #TO DO: return optimal launch angle theta
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

    
    return (x_target - x_hit)**2