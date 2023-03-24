import math
import sympy as sym
g = 9.81 

#legacy functie, mag weg
def find_compression(v0,theta):
    x, k = sym.symbols("x k")
    f = k*x**2 - 0.981*math.cos(theta)*x - 0.05*81
    k_val = 700
    x_sol = sym.solve(f,x)[0]
    x_val = x_sol.subs(k,k_val)
    return x_val 

def find_elongation(v0,theta,k = 700, m = 0.050, n = 1,r_ball = 0.064, rho = 1.29, Cd = 0.6 , mu_k = 0.4):
    
    x = sym.symbols("x")
    #De volgende vergelijking is afgeleid uit de formule van arbeid en energie, waarbij bepaalde krachten inwerken, zie dossier fysisch model voor gedetailleerde uitleg.
    #x = 0.15
    
    #Function = n*k/(2*m) * x**2 - (g*math.sin(theta) + rho/(2*m) * Cd * (math.pi*r_ball**2 )* v0**2 + mu_k * g * math.cos(theta)) * x - 1/2*v0**2 
    Function = n * k/2 * x**2 - rho/(2*m) * Cd * (math.pi*r_ball**2 )* v0**2 * x - m * g * math.sin(theta) * x  - m/2 * v0**2 
    #vind delta x, de benodigde uitrekking, aangezien dit de enige onbekende is.
    
    sol = sym.solve(Function, x)
    sol = max(sol)
    return sol