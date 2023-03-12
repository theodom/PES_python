from schuineWorp import create_bounce, create_plot, get_emmers
from determineAngle import optimize
from launchMechanism import find_compression, find_elongation

emmerLijst = get_emmers()

"""
Tenzij anders aangegeven zijn alle grootheden in SI-eenheden.
"""

#input waarden
v0 = float(input("geef de beginsnelheid in: "))
xt = 12
yt = 0.3
emmer = float(input("Kies een doelwit (1-6): "))
xt = emmerLijst[emmer-1]


launch_angle = optimize(v0,xt,yt)

#visualiseer
x,y = create_bounce(v0,launch_angle)
x_g, y_g = create_bounce(v0,45)  
create_plot(x,y,x_guess=x_g, y_guess=y_g,x_target=xt,y_target=yt)
x = round(find_elongation(9,30,k= 450,n = 2)[1]*100,2)
print(x)

print("move the spring",x, "cm backwards.")
