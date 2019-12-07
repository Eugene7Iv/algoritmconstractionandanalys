import math
import numpy as np

func = math.cosh
  
def internalSum(function, valuesU):
    l = [function(value) for value in valuesU]
    res = sum(l)
    return res

def externalSum(function, U):
    l = [internalSum(function, ux) for ux in U]
    res = sum(l)
    return res
    
   
def integr(n,iterCount_ = 1000):
    U = []
    h = 1 / n
    for i in range(0, n):
        U.append([])
        for j in range(0 , n):
            if i == n - 1:
                U[i].append(1)
            elif j == 0 or j == n - 1 or i == 0:
                U[i].append(0)
            else:
                U[i].append(0.5)

    for k in range(0, iterCount_):
        I = 0.5*(h**6)*(externalSum(func, U))**2
        for i in range(1, n - 1):
            for j in range(1 , n - 1):
                U[i][j] = 0.25*(U[i + 1][j] + U[i - 1][j] + U[i][j + 1] + U[i][j - 1] - I)
                
    return U
                
    
