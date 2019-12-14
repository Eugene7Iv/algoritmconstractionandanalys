import random
import time
from environment import *

env1 = Environment()
env1.loadGraphFromTxt("TSP/test100.txt")

sizeColony = int(input("Enter size of ant colony : "))
startNode = int(input("Enter started node (can be less than zero) : "))

env1.initAntColony(sizeColony)
if env1.locateAnt() :
#    env1.showColony()
    print("-------Exploring-------")
    time.clock()
    env1.startExploring(100)
    print("-------EndExploring-------")
    print("spend time : ", time.clock())
    print("-------startColonysTravel-------")
    env1.startColonysTravel(node = startNode)
    print("-------endColonysTravel-------")
    print("spend time : ", time.clock())

    env1.printResume()
#   env1.showColony()