from simpelModel import create_bounce, create_plot
import math
from scipy.optimize import newton
import scipy.optimize as spo
import numpy as np
import matplotlib.pyplot as plt

#user inputs:
v0 = float(input("starting velocity: "))
launch_angle = float(input("starting angle: "))

x_target = 12
y_target = 0.3

def angle_to_hit_target(theta):
    x, y = create_bounce(v0,theta)
    x_hit = 0
    prev_hit = 0
    t = np.linspace(0,10,1000)
    x_hit = 0
    close = (y_target < y + 0.01) & (y < y_target + 0.01)
    #close = y_target
    print("cl: ",close)
    i = np.where(y == close)
    print("where: ",i)
    close_x = x[i]
    if close_x - 0.2 < x_target and close_x + 0.2 > x_target:
        x_hit = close_x[0]
        return
theta = np.linspace(0,90,90)

plt.plot(theta,angle_to_hit_target(theta))
#result = spo.differential_evolution(angle_to_hit_target, bounds=[(1,90)])

#print("res x= ",result.x)

#x, y = create_bounce(v0,result.x)
#create_plot(x,y)  
x, y = create_bounce(v0,launch_angle)
create_plot(x,y)