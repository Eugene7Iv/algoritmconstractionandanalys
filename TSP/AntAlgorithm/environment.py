from ant import Ant
from random import randint
from config import *
import time

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

    def locateAnt(self, ant, node):
        if node > -1:
            ant.takeStartedNode(node)
        else:
            colonySize = len(self.__colony)
            if colonySize < self.__size:
                node = randint(0, self.__size - 1)
            else:
                node = ant.getIndx() % self.__size
            ant.takeStartedNode(node)

    def locateAnts(self, node = -1):
        size = self.__size
        if size == 0:
            print("ERROR : graph is non defined")
            return False

        for ant in self.__colony:
            self.locateAnt(ant, node)

        return True

    def startColonysTravel(self, node = -1):
        tick = time.time()
        for ant in self.__colony:
            self.locateAnt(ant, node)
            ant.toStart()
            ant.travel()

            if NEED_PRINT_TRAVELED_WAY:
                self.__printAntInfo(ant)

        if NEED_PRINT_TIME_FOR_COLONYS_TRAVEL:
            print("----TIME FOR startColonysTravel(node) : ", time.time() - tick, " ----")


    def startExploring(self, iterCount, node = -1):
        tick = time.time()
        for i in range(iterCount):
            self.startColonysTravel(node = node)

            if NEED_PRINT_PhM:
                print("---------")
                print(self.__phMatrix)
                print("---------")
        
        if NEED_PRINT_TIME_FOR_EXPLORING:
            print("----TIME FOR startExploring(time, node) : ", time.time() - tick, " ----")

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