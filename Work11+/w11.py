import matplotlib.pyplot as plt
from numpy import *
import math

def fun(x):
  # cos(4*x)-x+1 - function
  f = x**1
  return f

x = linspace(-5, 5, 1000)
y = cos(4*x)-x+1
yx = fun(x)


plt.plot(x, y, label='cos(4*x)-x+1')
plt.plot(x, yx, label='x**3')
plt.legend()
plt.title('Taylor Expansion')
plt.grid()
plt.show()


