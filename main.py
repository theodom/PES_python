import schuineWorp as sw

v0 = float(input("donne une vitesse initiale: "))
launch_angle = float(input('donne une angle initiale: '))

x,y = sw.create_bounce(v0,launch_angle)
sw.create_plot(x,y)

