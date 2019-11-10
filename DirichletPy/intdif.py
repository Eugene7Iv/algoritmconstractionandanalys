from math import cosh

def solIntDif(n_ = 10, iterCount_ = 500, writeToFile = False):
    n = n_
    h = 1 / n
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

    sum = 0
    for k in range(0, iterCount):
        for i in range(1, n - 1):
            for j in range(1 , n - 1):
                for l in range(0, n):
                    for m in range(0, n):
                        sum += cosh(U[l][m])
                        sum *= h*h
                U[i][j] = 0.25*(U[i + 1][j] + U[i - 1][j] + U[i][j + 1] + U[i][j - 1] - sum)

    if(writeToFile):
        solFile = open('solFileIntDif.txt' , 'w')

        for i in range(0, n):
            for j in range(0 , n):
                solFile.write('%4f' % U[i][j] + '\t')
            solFile.write('\n')
        
        solFile.close
        
    return U