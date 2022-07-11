import numpy as np
import matplotlib.pyplot as plt
# Data for a three dimensional line
ax = plt.axes(projection='3d')
z = np.linspace(0, 15, 100)
x = np.sin(z)
y = np.cos(z)
ax.plot(x, y, z, color='gray', label='My Curve')

# Data for three dimensional scattered points
x1 = np.sin(z) + 0.1 * np.random.randn(100)
y1 = np.cos(z) + 0.1 * np.random.randn(100)
ax.scatter3D(x1, y1, z, c=z, cmap='jet', label='My Points')
plt.show()