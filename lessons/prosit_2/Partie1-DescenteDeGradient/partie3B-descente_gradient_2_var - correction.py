import math 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

# norm of a vector U in R^2
def norm2(U):
    return math.sqrt(U[0]**2 + U[1]**2)

# norm of a vector U in R^n
def norm(U):
    n = len(U)
    res = 0.0
    for i in range(n):
        res = res + U[i]**2
    return sqrt(res)

# Algorithm looking for the minimum of a function f of two variables with gradient descent
def GradientDescent(f, gradf, x, y, alpha=1e-2, eps=1e-6, maxIter=1000, disp=False):
    # grad_f : gradient of f
    # x, y : initial values choosen by the user
    # alpha : learning rate (give the speed of the descent)
    # eps : precision
    # maxIter : maximum number of iterations
    # disp : parameter to display steps of computations

    N = norm2(gradf(x, y))
    i=0
    while N>eps:
        gradfx, gradfy = gradf(x,y)
        N = norm2(gradf(x,y))
        x = x - alpha*gradfx
        y = y - alpha*gradfy        
        if disp:
            print("  Step ", i, ": [x, y, gradf(x), gradf(y)] = [", x, ", ", y , ", ", gradfx, ", ", gradfy, "]")
        if i > maxIter:
            print("Failure of gradient descent after", maxIter, "iterations")
            return None
        i += 1
    return x, y

# Algorithm looking for the minimum of a function f of two variables with gradient descent, gradient unknown
def GradientDescent2(f, x, y, alpha=1e-2, eps=1e-6, maxIter=1000, disp=False):
    # x, y : initial values choosen by the user
    # alpha : learning rate (give the speed of the descent)
    # eps : precision
    # maxIter : maximum number of iterations
    # disp : parameter to display steps of computations
    
    N = 2*eps # just to start the loop
    i=0
    while N>eps:
        gradfx = ( f(x+eps,y) - f(x-eps,y) ) / (2*eps) #numerical approximation of df/dx
        gradfy = ( f(x,y+eps) - f(x,y-eps) ) / (2*eps) #numerical approximation of df/dy
        N = norm2([gradfx, gradfy])
        x = x - alpha*gradfx
        y = y - alpha*gradfy
        if disp:
            print("  Step ", i, ": [x, y, gradf(x), gradf(y)] = [", x, ", ", y , ", ", gradfx, ", ", gradfy, "]")
        if i > maxIter:
            print("Failure of gradient descent after", maxIter, "iterations")
            return None
        i += 1
    return x, y


### TESTS with two variables ###
# on functions where the minimum is obvious to check if the code is okay

# f1 must be at his minimum in (1,1)
def f1(x, y):
    return (1-x)**2+(y-x**2)**2

def grad_f1(x, y):
    return 2*(2*x**3+x-2*x*y-1) , 2*(y-x**2) # = df/dx , df/dy

# f2 must be at his minimum in (0,0)
def f2(x, y):
    return -np.exp(-x**2 - y**2)

# modify parameters to test, we start at (1/2,1/2)
print("Coordinates of minimum of f1:")
print("  ", GradientDescent(f1, grad_f1, 0.5, 0.5, alpha=0.1))
print("  ", GradientDescent2(f1, 0.5, 0.5, maxIter=10000))
print("Coordinates of minimum of f2:")
print("  ", GradientDescent2(f2, 0.5, 0.5, alpha=0.01, maxIter=10000))

