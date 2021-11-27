import math
def F(x):
    return 9*x**4+8*x**3+1.5*x**2+2*x-10 # f(x)

def D1(x):
    return 36*x**3+24*x**2+3*x+2 # f'(x)

def D2(x):
    return 108*x**2+48*x+3 # f''(x)

def metKomb(a, b):
    if D1(a) * D2(a) < 0:
        a0 = b
        b0 = a
    else:
        a0 = a
        b0 = b
    xp1 = (a0 - F(a0)) / D1(a0) #a1
    xp2 = (b0 - F(b0) * (b0 - a0)) / (F(b0) - F(a0)) #b1
    while xp2 - xp1 < 0.0001:
        xn1 = (xp1 - F(xp1) * (xp2 - xp1)) / (F(xp2) - F(xp1))
        xn2 = xp2 - F(xp2 / D1(xp2))
        xp1 = xn1
        xp2 = xn2
    x = (xp1 + xp2) / 2
    return print(' Metod: KOMBINOVANIY\n x = ', x)
metKomb(-2/3, 5)
