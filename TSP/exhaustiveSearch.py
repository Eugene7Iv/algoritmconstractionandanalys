import copy
from config import adjacencyMatrixFile

def parseAdjM(file): 
    adjM = [list(map(float,item.split())) for item in file.read().splitlines()]

    return adjM

def calcDistance(nodes):
    L = 0
    for i in range(0, nodeCount):
        L += adjM[nodes[i]][nodes[i + 1]]
    
    return L

def start(outNode : int , vNode = []):
    visitedNode = copy.deepcopy(vNode)
    visitedNode.append(outNode)
    vNodesTemp = []
    minL = -1

    for node in range(nodeCount):
        if node not in visitedNode:
            res = start(node, visitedNode)
            if minL == -1:
                minL = res[0]
                vNodesTemp = res[1]
            else:
                if(res[0] < minL):
                    minL = res[0]
                    vNodesTemp = res[1]

    if len(visitedNode) == nodeCount:
        visitedNode.append(startNode)
        L = calcDistance(visitedNode)
        print(L , visitedNode)
        return L , visitedNode

    res = minL , vNodesTemp

    return res

adjMFile = open(adjacencyMatrixFile, 'r') #it's reading adjacency matrix
adjM = parseAdjM(adjMFile)
adjMFile.close()

adjMTemp = copy.deepcopy(adjM)

nodeCount = len(adjM)

startNode = int(input("StartNode = "))
print("Exhaustive search")
print(start(startNode))
input()