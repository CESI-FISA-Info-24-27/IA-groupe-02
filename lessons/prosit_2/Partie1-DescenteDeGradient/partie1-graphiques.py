import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D



def f1(x, y):
    return np.exp(-x**2 - y**2)

# maillage des couples de points (x,y) pour représenter f1: [-2,2]x[-2,2] -> R
x,y = np.meshgrid(np.linspace(-2,2,200), np.linspace(-2,2,200))
z = f1(x,y)

# représentation graphique de la surface z = f1(x,y) dans l'espace
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title('Courbes de la fonction f(x,y))')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z = f(x,y)')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()

# représentation graphique de la courbe de niveau de f
fig,ax = plt.subplots(1, 1, figsize=(8,8))
cp = ax.contourf(x, y, z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title(' Courbes de niveau de f(x,y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()


def f2(x, y):
    return (1-x)**2 + (y-x**2)**2

# maillage des couples de points (x,y) pour représenter f1: [-1,1]x[-1,2] -> R
x,y = np.meshgrid(np.linspace(-1,1,200), np.linspace(-1,2,200))
z = f2(x,y)

# représentation graphique de la surface z = f1(x,y) dans l'espace
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title('Courbes de la fonction f(x,y))')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z = f(x,y)')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()

# représentation graphique de la courbe de niveau de f
fig,ax = plt.subplots(1, 1, figsize=(8,8))
cp = ax.contourf(x, y, z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title(' Courbes de niveau de f(x,y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

