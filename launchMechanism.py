import math
import sympy as sym
g = 9.81 

def find_compression(v0,theta):
    x, k = sym.symbols("x k")
    f = k*x**2 - 0.981*math.cos(theta)*x - 0.05*81
    k_val = 700
    x_sol = sym.solve(f,x)[0]
    x_val = x_sol.subs(k,k_val)
    return x_val 

def find_elongation(v0,theta,k = 700, m = 0.050, n = 1):
    #x = math.sqrt(m/(2*k))*v0
    x = sym.symbols("x")
    f = n*k/2 * ((x**2)) - m * g * x * math.sin(theta*math.pi/180) - m/2 * v0**2
    sol = sym.solve(f, x)
    return sol[-1]
