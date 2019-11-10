from math import pi, sinh, sin, sqrt

def solDirichlet(n_ = 10, iterCount_ = 100, writeToFile = False):
    n = n_
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

    if(writeToFile):
        solFile = open('solFile.txt' , 'w')

        for i in range(0, n):
            for j in range(0 , n):
                solFile.write('%4f' % U[i][j] + '\t')
            solFile.write('\n')
        
        solFile.close
        
    return U

def getDirichlet(n_, t_, h):
    supC = lambda n: 2 * (1 - (-1)^n) / (pi * n * sinh(pi * n))
    func = lambda x, y, n: supC(n) * sinh(pi * n * x) * sin(pi * n *y)


    ч = np.arange(0, 1, h)
    xlen = len(X)
    н = np.arange(0, 1, h)
    ylen = len(Y)
    x = []
    y = []
    h = 1 / (n_)

    for i in range(0, n_+1):
        x.append(i * h)
        y.append(i * h)
    print(x , '\n' , y)
    U = []

    for i in range(0, n_+1):
        U.append([])
        for j in range(0, n_+1):
            u = __sum(func, x[i], y[j], t_) + __sum(func, y[j], x[i], t_)
            U[i].append(u)

    return U

def __sum(function, x_, y_, k):
    func = function
    sum = 0
    t = 1

    while(t <= k):
        sum += func(x_, y_, t)
        t += 1
    
    return sum