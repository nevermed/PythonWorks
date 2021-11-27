import math 

def f1(x):
    return 9*x**4+8*x**3+1.5*x**2+2*x-10
def f2(x):
    return 36*x**3+24*x**2+3*x+2
    
def metHord(a, b):
    
    if f1(a) * f2(a) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
        
    xi1 = xi - (xi - x0) / (f1(xi) - f1(x0)) * f1(xi)
    
    while abs(xi1 - xi) >= 0.01:
        xi = xi1
        xi1 = xi - (xi - x0) / (f1(xi) - f1(x0)) * f1(xi)
            
    xk = f1(xi1)
    
    print('Hord Metod: ', xk)
    return xk
    
metHord(-2/3, 5)