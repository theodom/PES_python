import math
import numpy as np
from sympy import symbols
import matplotlib.pyplot as plt

#get input variables
v0 = float(input("begin velocity"))
launch_angle = float(input("launch angle in degrees"))
launch_angle = math.radians(launch_angle)
m = float(input("input ball mass"))
#constants
drag_coeff = 0.2
g = 9.81
t = symbols('t')

vel_array = np.array([v0,v0-g*t])
vx = vel_array(0)
vy = vel_array(1)
pos_array = np.array([vx*t , vy*t - g/2*t^2 ])

x_plt = np.linspace(0,20)
plt.plot(x_plt,pos_array)