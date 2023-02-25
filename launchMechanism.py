import math
import sympy as sym


def find_compression(v0,theta):
    x, k = sym.symbols("x k")
    f = k*x**2 - 0.981*math.cos(theta)*x - 0.05*81
    x_sol = sym.solve(f,x)[1]
    k_val = 500
    x_val = x_sol.subs(k,k_val)
    return x_val
