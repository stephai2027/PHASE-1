import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection = "3d")

x = np.linspace(-10,10,200)
y = np.linspace(-10,10,200)
X,Y = np.meshgrid(x,y)
Z = np.exp(-(X**2+Y**2))
ax.plot_surface (X,Y,Z)

#Affichage
plt.title('exemple de fonctions 3D')
plt.show()