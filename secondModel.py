import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from simpelModel import create_plot


#constants
g = 9.81 #zwaarteveldsterkte
AIR_RESISTANCE = 0
RESTITUTION_X = 0.59 # OPNIEUW VERIFIEREN
RESTITUTION_Y = 0.814  # NOG TE TESTEN
TIME = 4 #Aantal te simuleren seconden

def create_movement(v0, launch_angle, x0 = 0, y0 = 0,r_ball=0.064):
   
    t = np.linspace(0,TIME,1000*TIME) #creërt linspace met interval 1 ms
    
    launch_angle = math.radians(launch_angle) #te lanceren hoek, in graden ingegeven, hier omgezet naar radialen
    
    omega = 0 #hoesknelheid van de bal bij lanceren (rad/s)

    
    #maakt numpy arrays voor x,y, vx, vy.
    #zogezegd efficienter dan python lists
    x = np.zeros(1000*TIME) 
    y = np.zeros(1000*TIME)
    vx = np.zeros(1000*TIME)
    vy = np.zeros(1000*TIME)
    
    #vul beginvoorwaarden in, nodig om bv hoek te bepalen
    x[0] = x0 # in meter
    y[0] = y0 # in meter
    vx[0] = v0 * math.cos(launch_angle) # in m/s
    vy[0] = v0 * math.sin(launch_angle) # idem
    
    #itereert over het gehele tijds interval, beginnend op t0+1
    bounce_counter = 0 
    for i in range(1,len(t)):
        v = math.sqrt((vx[i-1])**2 + (vy[i-1])**2)
        if not (vx[i-1] and vy[i-1]) == 0:
            theta = math.atan(vy[i-1]/vx[i-1])
        ax,ay = calculate_acceleration(v,theta,omega)
        
        #indien de bal (onderkant) onder 0 gaat in verticale richting, is hij aan het botsen
        #en moet de snelheid dus omgekeerd worden
        if y[i-1] < 0:
            #stopt simulatie bij 2e botsing
            #enkel visueel handig, vermijd oneindige botsingen nadat de bal toch
            #in de emmer is beland (of ernaast), hoe dan ook is alles wat verder gebeurt niet nuttig
            if bounce_counter >= 1: 
                #vx[i] = 0
                vy[i] = 0
            else:
                #verminderd snelheden met de restitutie coeffecient
                #experimenteel is ondervonden dat deze dezelfde is voor x en y
                vx[i] = RESTITUTION_X * abs(vx[i-1])
                vy[i] = RESTITUTION_Y * abs(vy[i-1])
                y[i-1] = 0
                bounce_counter += 1
        else: 
            vx[i] = vx[i-1] + ax*t[1]
            vy[i] = vy[i-1] + ay*t[1]
        
        #opmerking: t[i] stelt dt voor, de (infinitesemale) sprong van tijd, aangezien t[i] - t[i-1] = delta t = t[1]
        x[i] = x[i-1] + vx[i]*t[1]
        y[i] = y[i-1] + vy[i]*t[1]
    
    return x, y


def calculate_acceleration(v,theta,omega, m = 0.050, g = 9.81,r_ball = 0.064, rho = 1.29):
    
    ku = 0.75 #from  doi 10.1119/1.4974126
    Cd = 0.6 #drag coeff, semi-arbitrary
    

    kd =  Cd/2 * (math.pi*r_ball**2)*rho
    if v == 0:
        km = 0
    else: 
        km =  ku* omega*r_ball/(2*v) * (math.pi*r_ball**2)*rho
        km = 0.0003

    Fd = kd * v**2 # kracht tgv luchtweerstand
    Fm = km * v**2 # kracht tgv magnus effect oftewel spin

    #ogenblikkelijke versnelling in x en y
    ax = - (Fd + Fm)*math.cos(theta)/m
    ay = - g - (Fd + Fm)/m*math.sin(theta)
    
    return ax, ay

def plot_graph(x,y,x_target= 12, y_target = 0.3):
    _,ax = plt.subplots()
    plt.xlim(0,15)
    plt.ylim(0,4.5)
    plt.xlabel("horizontale afstand (m)")
    plt.ylabel("hoogte (m)")
    #plt.title("ball trajectory")
    rect = patches.Rectangle((x_target-0.1, 0),0.2,y_target,linewidth=1,edgecolor= 'black',facecolor="none")
    ax.add_patch(rect)
    ax.plot(x,y,color="blue")
    plt.show()
    return

def determine_distance(x,y,x_target,y_target,theta):
    #TODO: optimise launch angle in function of starting velocity
    bounced = False
    t = np.linspace(0,TIME,1000*TIME)
    for i in range (len(t)):
        if y_target - 0.01 < y[-i] and y[-i] < y_target + 0.01:
            bounced = True
        
        if bounced == True:
            print("x: ",x[-i] , " ; y: ",y[-i], "; theta: ",theta, " d: ",x_target-x[-i])
            return x_target - x[-i]
    return x_target

def optimise_angle(v0,x_target,y_target):
    theta_distance = dict()
    for i in range(1,360):
        theta = float(i/4)
        x,y = create_movement(v0,theta)
        distance = determine_distance(x,y,x_target,y_target,theta)
        
        theta_distance[theta] = distance
    best_angle = min(theta_distance, key= lambda k: theta_distance[k])
    while len(theta_distance) > 10:
        theta_distance.pop(max(theta_distance, key= lambda k: theta_distance[k]))
    print("angles: ",theta_distance)
    return best_angle
        
