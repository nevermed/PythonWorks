import numpy as np
import matplotlib.pyplot as plt

N = 10  
n = 2

k = 0.5    
b = 2     


y  = np.array([1.82,1.67,1.49,1.06,0.57,0.08,-0.33,-0.64,0.225,0.08])
x = np.array([0.1,0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.47,0.5])
f = np.array([k*z+b for z in range(n)])



mx = x.sum()/N
my = y.sum()/N
a0 = np.dot(x.T, x)/N
a1 = np.dot(x.T, y)/N

kk = (a1 - mx*my)/(a0 - mx**2)
bb = my - kk*mx
ff = np.array([kk*z+bb for z in range(n)])

plt.scatter(x, y, s=10, c='g')

plt.plot(ff, c='r')
plt.grid(True)
plt.show()