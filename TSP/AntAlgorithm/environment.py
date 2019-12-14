from ant import Ant
from random import randint
from config import *

class Environment:
    def __init__(self):
        self.__size = 0
        self.__adjMatrix = None
        self.__colony = []
        self.__phMatrix = None

    def loadGraphFromTxt(self, fileName):
        fileTxt = open(fileName, 'r')
        self.__adjMatrix = self.__parseFile(fileTxt)
        fileTxt.close()

        self.__size = len(self.__adjMatrix)
        self.__phMatrix = [[0.2 for i in range(self.__size)] for i in range(self.__size)]        

    def initAntColony(self, count):
        for i in range(count):
            self.__colony.append(Ant(self))

    def locateAnt(self):
        size = self.__size
        if size == 0:
            print("ERROR : graph is non defined")
            return False

        colonySize = len(self.__colony)

        for i in range(colonySize):
            if colonySize < self.__size:
                node = randint(0, self.__size - 1)
            else:
                node = i % self.__size
            self.__colony[i].takeStartedNode(node)

        return True

    def startColonysTravel(self, node = -1):
        for ant in self.__colony:
            if node > -1:
                ant.takeStartedNode(node)
                ant.toStart()
            ant.traveling()
            if needPrintTraveledWay:
                self.__printAntInfo(ant)


    def startExploring(self, time):
        colonySize = len(self.__colony)
        for i in range(time):
            if needPrintPhM:
                print("---------")
                print(self.__phMatrix)
                print("---------")
            for ant in self.__colony:
                ant.traveling()
                if needPrintExploredWay:
                    self.__printAntInfo(ant)
                if colonySize < self.__size:
                    ant.takeStartedNode(randint(0, self.__size - 1))
                ant.toStart()

    def showColony(self):
        for i in range(len(self.__colony)):
            print("ant : ",self.__colony[i].getIndx()," his place : ", self.__colony[i].getStartNode())
    
    def printResume(self):
        print("Amount of nodes : ", self.__size)
        print("Size of colony : ", len(self.__colony))
        minimal = self.__getMinWalkedDistance()
        print("minimal : ", end='\n')
        print("indx of ant : ", minimal[0], end='\n')
        print("way : ", minimal[1], end='\n')
        print("distance : ", minimal[2], end='\n')

    def __parseFile(self,file): 
        adjM = [list(map(float,item.split())) for item in file.read().splitlines()]

        return adjM

    def __getMinWalkedDistance(self):
        minAnt = [self.__colony[0].getIndx() ,self.__colony[0].getWay(), self.__colony[0].getWalkedDistance()]

        for ant in self.__colony:
            distance = ant.getWalkedDistance()
            if distance < minAnt[2]:
                minAnt = [ant.getIndx() ,ant.getWay(), ant.getWalkedDistance()]

        return minAnt

    def __printAntInfo(self, ant):
        print("---------")
        print("indx of ant : ", ant.getIndx())
        print("way : ", ant.getWay())
        print("distance : ", ant.getWalkedDistance())


    def getNodeCount(self):
        return self.__size

    def getAdjM(self):
        return self.__adjMatrix

    def getPhM(self):
        return self.__phMatrix                