from simpelModel import create_bounce, create_plot, get_emmers
from secondModel import create_movement, optimise_angle
from determineAngle import optimize
from launchMechanism import find_compression, find_elongation



"""
Tenzij anders aangegeven zijn alle grootheden in SI-eenheden.
"""

#input waarden
emmerLijst = get_emmers()
v0 = float(input("geef de beginsnelheid in: "))
emmer = int(input("Kies een doelwit (1-6): "))

#bepaal welke de coördinaten van het doel zijn.
xt = emmerLijst[emmer-1]
yt = 0.3

"""
momenteel wordt er in main.py enkel gebruik gemaakt van het realistischere "secondModel", er zijn dus enkele imports die niet gebruikt zijn,
Deze blijven echter staan om snel en eenvoudig te kunnen overschakelen indien nodig. 
"""
launch_angle = optimise_angle(v0,xt,0.3)
print(launch_angle)

#visualiseer
#x,y = create_bounce(v0,launch_angle)
x, y = create_movement(v0,launch_angle)
#creër een referentieworp van 45° lanceringshoek
x_g, y_g = create_movement(v0,45)

#bepaal welke uitrekking nodig is om v0 te behalen. In het reële mechanisme
# is x normaal gezien constant, maar dit dient als referentie voor de haalbaarheid
x = round(find_elongation(v0,launch_angle,k= 450,n = 3)*100,2)
print("move the spring",x, "cm backwards.")

create_plot(x,y,x_guess=x_g, y_guess=y_g,x_target=xt,y_target=yt)

