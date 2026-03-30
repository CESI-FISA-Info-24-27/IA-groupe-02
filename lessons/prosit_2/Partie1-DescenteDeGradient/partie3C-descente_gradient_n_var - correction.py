import math 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

# norm of a vector U in R^n
def norm(U):
    n = len(U)
    res = 0.0
    for i in range(n):
        res = res + U[i]**2
    return sqrt(res)

# Algorithm looking for the minimum of a function f of n variables with gradient descent
def GradientDescentMulti(f, gradf, X, alpha=1e-2, eps=1e-6, maxIter=1000):
    # gradf : gradient of f
    # X : initial vector values choosen by the user
    # alpha : learning rate (give the speed of the descent)
    # eps : precision
    # maxIter : maximum number of iterations
    N = norm(gradf(X))
    i=0
    while N>eps:
        X = X - alpha*gradf(X)
        N = norm(gradf(X))
        if i > maxIter:
            print("Failure of gradient descent after", maxIter, "iterations")
            return None
        i += 1
    return X

# Algorithm computing an approximation of the gradient of f
def MultiGradient(f, X, eps=1e-6):
    n = len(X)
    Grad = np.zeros(n)
    for i in range(n):
        Eps = np.zeros(n)
        Eps[i] = eps
        Grad[i] = ( f(X+Eps) - f(X-Eps) ) / (2*eps)
    return Grad

# Algorithm looking for the minimum of a function f of n variables with gradient descent, gradient unknown
def GradientDescentMulti2(f, X, alpha=1e-2, eps=1e-6, maxIter=1000):
    # X : initial vector values choosen by the user
    # alpha : learning rate (give the speed of the descent)
    # eps : precision
    # maxIter : maximum number of iterations
    # disp : parameter to display steps of computations
    N = 2*eps # just to start the loop
    i=0
    while N>eps:
        gradf = MultiGradient(f, X, eps)
        N = norm(gradf)
        X= X - alpha*gradf
        if i > maxIter:
            print("Failure of gradient descent after", maxIter, "iterations")
            return None
        i += 1
    return X

## TESTS with two variables ##
# on functions where the minimum is obvious to check if the code is okay
# this part checks if what we've done in part 3B can be done with our new function

# f1 must be at his minimum in (1,1)
def f1(X):
    x = X[0]
    y = X[1]
    return (1-x)**2+(y-x**2)**2

def grad_f1(X):
    x = X[0]
    y = X[1]
    return np.array([2*(2*x**3+x-2*x*y-1) , 2*(y-x**2)]) # = df/dx , df/dy

# f2 must be at his minimum in (0,0)
def f2(X):
    x = X[0]
    y = X[1]
    return -np.exp(-x**2 - y**2)

# modify parameters to test, we start at (1/2,1/2)
X = np.array([0.5,0.5])
print("Coordinates of minimum of f1:")
print("  ", GradientDescentMulti(f1, grad_f1, X, alpha=0.1))
print("  ", GradientDescentMulti2(f1, X, alpha=0.1))
print("Coordinates of minimum of f2:")
print("  ", GradientDescentMulti2(f2, X, alpha=0.01, maxIter=10000))


### TESTS with three variables ###
# on functions where the minimum is obvious to check if the code is okay

# f3 must be at his minimum in (1,1,0)
def f3(X):
    x = X[0]
    y = X[1]
    z = X[2]
    return (1-x)**2+(y-x**2)**2+z**2

def grad_f3(X):
    x = X[0]
    y = X[1]
    z = X[2]
    return np.array([2*(2*x**3+x-2*x*y-1) , 2*(y-x**2), 2*z]) # = df/dx , df/dy, df/dz

# f4 must be at his minimum in (1/2,1/28,0)
def f4(X):
    x = X[0]
    y = X[1]
    z = X[2]
    return (0.5-x)**2 + (7*y-x**2)**2 + z**2

def grad_f4(X):
    x = X[0]
    y = X[1]
    z = X[2]
    return np.array([2*x-1+4*x**3-28*x*y,
                     14*(7*y - x**2),
                     2*z]) # = df/dx , df/dy, df/dz

# computations and display
X = np.array([0.5,0.5,0.5])
print("Coordinates of minimum of f3:")
print("  ", GradientDescentMulti(f3, grad_f3, X, maxIter=10000))
X = np.array([0, 0.5, 0.5])
print("Coordinates of minimum of f4:")
print("  ", GradientDescentMulti(f4, grad_f4, X, maxIter=10000))
print("  ", GradientDescentMulti2(f4, X, maxIter=10000))


def twoVarLinearRegression(A, X, Y):
    m = len(X)
    res = 0
    for i in range(m):
        res = res + (A[0]*X[i] + A[1] - Y[i])**2
    return res

