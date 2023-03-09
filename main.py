from schuineWorp import create_bounce, create_plot
from determineAngle import optimize
from launchMechanism import find_compression, find_elongation

#input waarden
v0 = float(input("geef de beginsnelheid in: "))
xt = 12
yt = 0.3


launch_angle = optimize(v0,xt,yt)
#launch_angle = 30
#visualiseer
x,y = create_bounce(v0,launch_angle)
x_g, y_g = create_bounce(v0,45)
create_plot(x,y,x_guess=x_g, y_guess=y_g,x_target=xt,y_target=yt)
print("move the spring ",float(int(find_elongation(v0,k = 1400)*1000)/10.0), "cm backwards.")