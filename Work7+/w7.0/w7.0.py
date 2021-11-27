import matplotlib.pyplot as plt 
from numpy import *

def y(x):
   return x*sin(5*x)
x = linspace(-2, 5, 51)
y = y(x)
plt.plot(x, y, 'go-', label = 'Y(x)=x^cos(x^2)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plotting with markers')
plt.legend(['x*sin(5*x)'])
plt.show()