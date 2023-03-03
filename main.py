from schuineWorp import create_bounce, create_plot
from determineAngle import optimize

#input waarden
v0 = float(input("geef de beginsnelheid in: "))
xt = 12
yt = 0.3


launch_angle = optimize(v0,xt,yt)

#visualiseer
x,y = create_bounce(v0,launch_angle)
x_g, y_g = create_bounce(v0,45)
create_plot(x,y,x_guess=x_g, y_guess=y_g,x_target=xt,y_target=yt)
