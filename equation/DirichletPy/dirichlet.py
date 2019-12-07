from math import pi, sinh, sin, sqrt
import numpy as np

def solDirichlet(n, iterCount_ = 1000):
    iterCount = iterCount_

    U = []

    for i in range(0, n):
        U.append([])
        for j in range(0 , n):
            if (i == 0 or j == 0):
                U[i].append(0)
            elif (i == n - 1 or j ==  n- 1):
                U[i].append(1)
            else:
                U[i].append(0.5)

    for k in range(0, iterCount):
        for i in range(1, n - 1):
            for j in range(1 , n - 1):
                U[i][j] = 0.25*(U[i + 1][j] + U[i - 1][j] + U[i][j + 1] + U[i][j - 1])
        
    return U

def getDirichlet(X, Y):
    supC = lambda n: 2 * (1 - (-1)^n) / (pi * n * sinh(pi * n))
    func = lambda x, y, n: supC(n) * sinh(pi*n*x) * sin(pi*n*y)
    supCC = lambda n: 4 / (pi * n * sinh(pi * n))
    funcc = lambda x, y, n: supCC(2*n-1) * sinh(pi*(2*n-1)*x) * sin(pi*(2*n-1)*y)

    U = []

    n = len(X)

    for i in range(0, n):
            U.append([])
            for j in range(0 , n):
                if (i == 0 or j == 0):
                    U[i].append(0)
                elif (i == n - 1 or j ==  n- 1):
                    U[i].append(1)
                else:
                    u = sum(funcc, X[i], Y[j]) + sum(funcc, Y[j], X[i])
                    U[i].append(u)

    return U

def sum(function, x, y):
    func = function
    sum = 0
    t = 1

    while(True):
        s = func(x, y, t)
        sum += s
        t += 1
        if (s == 0):
            return sum

def error(U, G):
    n = len(U)
    eMax = 0.0
    for i in range(n):
        for j in range(n):
            e = abs(U[i][j]-G[i][j])
            if e > eMax:
                eMax = e
            #print(e)

    return eMax
    