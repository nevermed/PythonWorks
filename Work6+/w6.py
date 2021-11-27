from scipy import optimize
import math
def f1(x):
    return((2-math.cos(y)/2))
def f2(y):
    return(math.sin(x+1)-1.2)
def d1(x):
    return((2-math.cos(y)/2))
def d2(y):
    return(math.sin(x+1)-1.2)
if abs(d1(1.5)) < 1:  
    n = 1
    x0 = 0.5
    y0 = 0.2
    r = 1
    print('y 0 = ',x0)
    print('x 0 = ',y0)
    while r > 0.0001:
        xn = f2(y0)
        r = abs(xn - x0)
        x0 = xn
        print('y', n ,'= ',xn)
        
        while r > 0.0001:
            yn = f1(xn)
            r = abs(xn - x0)
            y0 = yn
            print('x', n ,'= ',yn)
            n = n + 1


def fun(x): 
    return[math.sin(x[0]+1)-1.2, math.sin(x[0]+1)-1.2]
sol = optimize.root(fun, [0.5, 0.2], method= 'hybr')
print(sol.x)