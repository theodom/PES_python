import math
import sympy as sym


def find_compression(v0,theta):
    x, k = sym.symbols("x k")
    f = k*x**2 - 0.981*math.cos(theta)*x - 0.05*81
    x_val = 0.1
    x_sol = sym.solve(f,k)[0]
    k_val = x_sol.subs(x,x_val)
    return k_val 
