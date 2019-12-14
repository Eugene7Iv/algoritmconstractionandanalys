import random
from config import *


class Ant:
    __count = -1

    def __init__(self, env):
        Ant.__count += 1
        self.__brain = AntBrain(env)
        self.__indx = Ant.__count

    def step(self, startNode):
        nextNode = self.__brain.chooseWay(startNode)
        self.__brain.keepNode(nextNode)
        self.__brain.updateWalkedDistance()
        return nextNode

    def traveling(self):
        startNode = self.__brain.getStartNode()
        node = self.step(startNode)
        while(node != startNode):
            node = self.step(node)

        visitedNodes = self.__brain.getMind()
        distance = self.__brain.getWalkedDistance()
        self.dropPheromone(visitedNodes, distance)

    def takeStartedNode(self,node):
        self.__brain.setStartNode(node)
        self.__brain.keepNode(node)

    def dropPheromone(self,vNodes, distance):
        q = 1
        ro = 0.7
        tau = self.__brain.getPhM()
        dT = q / distance # this is piece pheromone that ant droped

        for i in range(len(vNodes) - 1):
            tau[vNodes[i]][vNodes[i+1]] = (1-ro)*tau[vNodes[i]][vNodes[i+1]] + dT
            tau[vNodes[i+1]][vNodes[i]] = (1-ro)*tau[vNodes[i+1]][vNodes[i]] + dT
        
    def toStart(self):
        self.__brain.forget()
        startNode = self.__brain.getStartNode()
        self.__brain.keepNode(startNode)

    def getIndx(self):
        return self.__indx

    def getStartNode(self):
        return self.__brain.getStartNode()

    def getWalkedDistance(self):
        return self.__brain.getWalkedDistance()

    def getWay(self):
        return self.__brain.getMind()
        

class AntBrain:

    def __init__(self, env):
        self.__mind = []
        self.__walkedDistance = 0
        self.__startNode = -1
        self.__env = env

    def chooseWay(self, outNode):
        
        def P(outNode : int, inNode : int , availableNodes):
            beta = 1
            alfa = 1 

            if inNode not in availableNodes:
                return 0

            adjM = env.getAdjM()
            tau = env.getPhM()
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

        nextNode = -1
        env = self.__env
        availableNodes = []

        for j in range(env.getNodeCount()):
            if not self.wasAt(j):
                availableNodes.append(j)
    
        if (len(availableNodes) == 0):
            return self.__startNode

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

    def wasAt(self, node):
        res = node in self.__mind
        return res

    def keepNode(self, node):
        self.__mind.append(node)

    def updateWalkedDistance(self):
        node1 = self.__mind[len(self.__mind) - 1]
        node2 = self.__mind[len(self.__mind) - 2]
        self.__walkedDistance += self.__env.getAdjM()[node1][node2]

    def forget(self):
        self.__mind.clear()
        self.__walkedDistance = 0

    def getStartNode(self):
        return self.__startNode

    def setStartNode(self, node):
        self.__startNode = node

    def getMind(self):
        return self.__mind

    def getWalkedDistance(self):
        return self.__walkedDistance

    def getPhM(self):
        return self.__env.getPhM()