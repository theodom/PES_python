from schuineWorp import create_bounce, create_plot
import math
from scipy.optimize import newton
import scipy.optimize as spo
import numpy as np

#user inputs:
v0 = float(input("starting velocity: "))
launch_angle = float(input("starting angle: "))

x_target = 12
y_target = 0.3

def angle_to_hit_target(theta):
    x, y = create_bounce(v0,theta)
    x_hit = 0
    prev_hit = 0
    t = np.linspace(0,10,500)
    for i in range(len(t)):
        
        if y_target - 0.02 < y[i] and y[i] < y_target + 0.2:
            prev_hit = x_hit
            x_hit = x[i]
        if x_hit > x_target: 
            x_hit = prev_hit
            break
    
    return x_target - x_hit

print("distance: ", angle_to_hit_target(launch_angle))   

def second_try_optimisation():
    
    for theta in range(0,90,0.5):
        #x,y : create_bounce(v0,theta)
        distance = angle_to_hit_target(theta)
        if math.abs(distance) < 0.2:
            return theta
    return "failed"

print("theta: ", second_try_optimisation())

#result = spo.minimize(angle_to_hit_target, 30)
#result = spo.differential_evolution(angle_to_hit_target, bounds=[(1,90)])

# if result.success:
#     print(f"x= {result.x} y = {result.fun}")
# else:
#     print("failure \n",result)

x_guess, y_guess= create_bounce(v0,launch_angle)
create_plot(x_guess,y_guess)
#print("res x= ",result.x)
# x, y = create_bounce(v0,result.x)
# create_plot(x,y)


#bronvermelding spo.minimize: https://www.youtube.com/watch?v=G0yP_TM-oag