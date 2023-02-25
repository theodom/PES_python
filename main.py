from schuineWorp import create_bounce, create_plot
from determineAngle import optimise_angle


#launch_angle = float(input('donne une angle initiale: '))

# x,y = sw.create_bounce(v0,launch_angle)
# sw.create_plot(x,y)


v0 = float(input("geef de beginsnelheid in: "))
#xt = float(input("afstand tot doel: "))
#yt = float(input("hoogte van het doel: "))
xt = 12
yt = 0.3

launch_angle = optimise_angle(v0,xt,yt)
print("launching at: ",launch_angle,"°")
x,y = create_bounce(v0,launch_angle)
create_plot(x,y)