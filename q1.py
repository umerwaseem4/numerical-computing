import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

data = np.loadtxt('bps.dat')  

x = data[:, 0]
y = data[:, 1]

cs = CubicSpline(x, y)

x_interp = np.linspace(min(x), max(x), 100) 
y_interp = cs(x_interp)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_interp, y_interp, label='Interpolated Curve')
plt.title('Cubic Spline Interpolation')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()