import math 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from pylab import *


xlist = np.arange(-2, 2, 0.25)
ylist = np.arange(-2, 2, 0.25)
x, y = np.meshgrid(xlist, ylist)

def f1(x, y):
    return np.exp(-x**2-y**2)
z = f1(x, y)

# représentation graphique de la surface z = f(x,y) dans l'espace
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title('Courbes de la fonction f(x,y) = exp(-x²-y²)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z = f(x,y)')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()


# représentation graphique de la courbe de niveau de f
fig,ax = plt.subplots(1, 1, figsize=(8,8))
cp = ax.contourf(x, y, z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title(' Courbes de niveau de f(x,y) = exp(-x²-y²)')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

# champ de vecteur (1,0) sur f
fig,ax = plt.subplots(1, 1, figsize=(8,8))
cp = ax.contourf(x, y, z)
q = ax.quiver(x, y, 1, 0)  # pour ajouter le champ de vecteur v = (1,0)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title(' Courbes de niveau et champ de vecteurs sur f(x,y) = exp(-x²-y²)')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

# champ de vecteur (x,y) sur f
fig,ax = plt.subplots(1, 1, figsize=(8,8))
cp = ax.contourf(x, y, z)
q = ax.quiver(x, y, x, y)  # pour ajouter le champ de vecteur v = (x,y)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title(' Courbes de niveau et champ de vecteurs sur f(x,y) = exp(-x²-y²)')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

# champ de gradient sur f
fig,ax = plt.subplots(1, 1, figsize=(8,8))
cp = ax.contourf(x, y, z)
q = ax.quiver(x, y, -2*x*f1(x,y), -2*y*f1(x,y)) # pour ajouter le champ de vecteur v = (x,y)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title(' Courbes de niveau et champ de gradients sur f(x,y) = exp(-x²-y²)')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
