from schuineWorp import create_bounce, create_plot
from determineAngle import optimize




v0 = float(input("geef de beginsnelheid in: "))
#manual_angle = float(input("manuele hoek: "))
xt = float(input("afstand tot doel: "))
yt = float(input("hoogte van het doel: "))
# xt = 12
# yt = 0.3



launch_angle = optimize(v0,xt,yt)

x,y = create_bounce(v0,launch_angle)
x_g, y_g = create_bounce(v0,45)
create_plot(x,y,x_guess=x_g, y_guess=y_g,x_target=xt,y_target=yt)


#reate_plot(x_test,y_test)
