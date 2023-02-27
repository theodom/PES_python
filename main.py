from schuineWorp import create_bounce, create_plot
from determineAngle import optimise_angle, optimize, determine_distance
from launchMechanism import find_compression


#launch_angle = float(input('donne une angle initiale: '))

# x,y = sw.create_bounce(v0,launch_angle)
# sw.create_plot(x,y)


v0 = float(input("geef de beginsnelheid in: "))
#manual_angle = float(input("manuele hoek: "))
#xt = float(input("afstand tot doel: "))
#yt = float(input("hoogte van het doel: "))
xt = 12
yt = 0.3


#usable_theta = []
#launch_angle = optimise_angle(v0,xt,yt, list=usable_theta)


#visualising results 
# print("launching at: ",launch_angle,"°")
# x,y = create_bounce(v0,launch_angle)
# x2, y2 = create_bounce(v0,manual_angle)
# print("wind the spring back by ",find_compression(v0,launch_angle)*100," cm")
# create_plot(x,y)


#old optimise function
#angle = optimise_angle(v0,xt,yt)
#x_old, y_old = create_bounce(v0,angle)
#create_plot(x_old,y_old)


launch_angle = optimize(v0,xt,yt)
#x_test,y_test = create_bounce(v0, 35.5)
#print(determine_distance(x_test,y_test,xt,yt))

x,y = create_bounce(v0,launch_angle)
create_plot(x,y)


#reate_plot(x_test,y_test)
