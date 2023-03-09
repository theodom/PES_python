import math
import sympy as sym


def find_compression(v0,theta):
    x, k = sym.symbols("x k")
    f = k*x**2 - 0.981*math.cos(theta)*x - 0.05*81
    k_val = 700
    x_sol = sym.solve(f,x)[0]
    x_val = x_sol.subs(k,k_val)
    return x_val 

def find_elongation(v0,k = 700, m = 0.050):
    x = math.sqrt(m/(2*k))*v0
    return x
