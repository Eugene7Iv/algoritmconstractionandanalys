import random
from datetime import datetime as dt


n = int(input("n = "))

adjM = []

for i in range(n):
    adjM.append([])
    for j in range(n):
        if (j > i):
            adjM[i].append(random.randint(1,100))
        elif (j < i):
            adjM[i].append(adjM[j][i])
        elif (j == i):
            adjM[i].append(0)

for i in range(n):
    for j in range(n):
        print(adjM[i][j], end = '\t')
    print('\n')

time = dt.strftime(dt.now(), "%Y_%m_%d_%H_%M_%S")

testFile = open("test" + str(n) + "_" + time + '.txt', 'w')

for i in range(n):
    for j in range(n):
        if (j != n - 1):
            testFile.write(str(adjM[i][j]) + '\t')
        else:
            testFile.write(str(adjM[i][j]))
    if i != n - 1:
        testFile.write('\n')    
testFile.close()