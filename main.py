from schuineWorp import create_bounce, create_plot
from determineAngle import optimise_angle


#launch_angle = float(input('donne une angle initiale: '))

# x,y = sw.create_bounce(v0,launch_angle)
# sw.create_plot(x,y)


v0 = float(input("geef de beginsnelheid in: "))
#manual_angle = float(input("manuele hoek: "))
#xt = float(input("afstand tot doel: "))
#yt = float(input("hoogte van het doel: "))
xt = 12
yt = 0.3
usable_theta = []
launch_angle = optimise_angle(v0,xt,yt, list=usable_theta)


#visualising results 
print("launching at: ",launch_angle,"°")
x,y = create_bounce(v0,launch_angle)
#x2, y2 = create_bounce(v0,manual_angle)
create_plot(x,y)