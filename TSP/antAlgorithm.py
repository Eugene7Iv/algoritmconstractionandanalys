import random
import copy

from config import *

startNode = int(input("StartNode = "))

#
# adjacency matrix parsing
#
def parseAdjM(file): 
    adjM = [list(map(float,item.split())) for item in file.read().splitlines()]

    return adjM

#
# return probability of transition from outNode to inNode
#
def P(outNode : int, inNode : int , availableNodes): 
    if inNode not in availableNodes:
        return 0

    l , t = adjM[outNode][inNode] , tau[outNode][inNode]
    n = 1 / l
    s = 0

    for node in availableNodes:
        s += pow(1 / adjM[outNode][node], beta) * pow(tau[outNode][node], alfa)

    if s == 0:
        return 100 * 1 / len(availableNodes)

    up = pow(n,beta) * pow(t,alfa)
    down = s
    res = 100 * up / down

    return res

#
# chooses way and return next node
#
def step(outNode : int , adjMTemp):
    availableNodes = []
    nextNode = -1

    for j in range(nodeCount):
        if  (adjMTemp[outNode][j] != 0):
            availableNodes.append(j)
    
    if (len(availableNodes) == 0):
        return startNode

    tranP = []
    segment = [0]

    for j in range(len(availableNodes)):
        inNode = availableNodes[j]
        tranP.append(P(outNode, inNode, availableNodes))
        segment.append(segment[j] + tranP[j])

    p = random.randint(0,100)

    for k in range(len(segment)):
        if p <= segment[k]:
            nextNode = availableNodes[k-1]
            break

    if nextNode == -1:
        nextNode = availableNodes[random.randint(0, len(availableNodes) - 1)]
    
    return nextNode

#
# return walked distance and visited nodes
#
def antTraveling(sNode : int):
    if(debug):
        print('-----------------new traveling----------------\n')

    adjMTemp = copy.deepcopy(adjM)
    visitedNodes = []

    currentNode = sNode
    visitedNodes.append(currentNode)
    for row in adjMTemp:
        row[currentNode] = 0

    nextNode = step(currentNode , adjMTemp)
    
    L = float(adjM[currentNode][nextNode])

    if(debug):
        print(f'distance from {currentNode} to {nextNode} = ',  adjM[currentNode][nextNode],'\n')
        print(f'total distance = ', L, '\n')

    visitedNodes.append(nextNode)

    for row in adjMTemp:
        row[nextNode] = 0
    adjMTemp[nextNode][currentNode] = 0

    currentNode = nextNode

    while (nextNode != sNode):
        nextNode = step(currentNode , adjMTemp)
        L += float(adjM[currentNode][nextNode])
        
        if(debug):
            print(f'distance from {currentNode} to {nextNode} = ',  adjM[currentNode][nextNode],'\n')
            print(f'total distance = ', L, '\n')

        for row in adjMTemp:
            row[nextNode] = 0
        adjMTemp[nextNode][currentNode] = 0
        currentNode = nextNode
        visitedNodes.append(nextNode)
        

    return L , visitedNodes

def printRes():
    print('L = ', minL,' visited nodes : ',vNodes)
    if  (printTotalIteration):
        print(f'totalIteration = {totalIteration}\ncount = {count}')
    if (writeToFile):
        resFile = open(resultFile, 'a')
        s = f'''-----------------------------{adjacencyMatrixFile}-----------------------------
        L = {minL}\nvisite nodes : {vNodes}\ntotalIteration = {totalIteration}\ncount = {count}\n'''
        resFile.write(s)
        resFile.close()

adjMFile = open(adjacencyMatrixFile, 'r') # reading adjacency matrix
adjM = parseAdjM(adjMFile)
adjMFile.close()

nodeCount = len(adjM)

tau = [[0 for i in range(nodeCount)] for i in range(nodeCount)] #initilizing matrix of pheromone

at = antTraveling(startNode) #it commit traveling from startNode
minL = float(at[0]) # this is distance that ant walked
vNodes = list(at[1]) # this is list of nodes that ant visited

dT = q / minL # this is piece pheromone that ant droped

tau[startNode][vNodes[0]] = (1-ro)*tau[startNode][vNodes[0]] + dT
tau[vNodes[0]][startNode] = (1-ro)*tau[vNodes[0]][startNode] + dT

for i in range(len(vNodes) - 1):
    tau[vNodes[i]][vNodes[i+1]] = (1-ro)*tau[vNodes[i]][vNodes[i+1]] + dT
    tau[vNodes[i+1]][vNodes[i]] = (1-ro)*tau[vNodes[i+1]][vNodes[i]] + dT

count = 0
totalIteration = 0

while True:
    totalIteration += 1
    prevMinL = float(minL)

    at = antTraveling(startNode)
    minL = float(at[0])
    vNodes = list(at[1])

    dT = q / minL

    tau[startNode][vNodes[0]] = (1-ro)*tau[startNode][vNodes[0]] + dT
    tau[vNodes[0]][startNode] = (1-ro)*tau[vNodes[0]][startNode] + dT

    for i in range(len(vNodes) - 1):
        tau[vNodes[i]][vNodes[i+1]] = (1-ro)*tau[vNodes[i]][vNodes[i+1]] + dT
        tau[vNodes[i+1]][vNodes[i]] = (1-ro)*tau[vNodes[i+1]][vNodes[i]] + dT

    if (prevMinL == minL):
        count += 1
    else:
        count = 0

    if (totalIteration > minNumberTreveling):
        if ((count == numberSameWalkedDistance) or (totalIteration == maxNumberTreveling)):
            break
print("Ant algorithm")

if (printTau):
    for i in range(nodeCount):
        for j in range(nodeCount):
            print(round(tau[i][j], 4), end = ' ')
        print('\n')
printRes()