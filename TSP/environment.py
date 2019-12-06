from ant import Ant
from random import randint

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

    def locateAnt(self, node = -1):
        size = self.__size
        if size == 0:
            print("ERROR : graph is non defined")
            return False

        if node != -1:
            for member in self.__colony:
                member.takeStartedPlace(node)
            return True


        for i in range(len(self.__colony)):
            if i >= self.__size:
                node = i - self.__size
            else:
                node = i
            self.__colony[i].takeStartedPlace(node)

        return True

    def startColonysTravel(self):
        for member in self.__colony:
            member.traveling()

    def startExploring(self, time):
        for i in range(time):
            print("---------")
            print(self.__phMatrix)
            print("---------")
            for member in self.__colony:
                member.traveling("Exploring")
                member.toStart()

    def showColony(self):
        for i in range(len(self.__colony)):
            print("ant : ",self.__colony[i].getIndx()," his place : ", self.__colony[i].getStartNode())

    def __parseFile(self,file): 
        adjM = [list(map(float,item.split())) for item in file.read().splitlines()]

        return adjM

    def getNodeCount(self):
        return self.__size

    def getAdjM(self):
        return self.__adjMatrix

    def getPhM(self):
        return self.__phMatrix