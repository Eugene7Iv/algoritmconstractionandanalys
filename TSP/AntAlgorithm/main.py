import random
import time
from environment import *

env1 = Environment()
env1.loadGraphFromTxt("TSP/test10.txt")

sizeColony = int(input("Enter size of ant colony : "))
timeForExplorint = int(input("Enter time for exploring : "))
startNode = int(input("Enter started node (can be less than zero) : "))

env1.initAntColony(sizeColony)
if env1.locateAnts(node = startNode) :
#    env1.showColony()
    print("-------Exploring-------")
    tick = time.time()
    env1.startExploring(timeForExplorint, node = startNode)
    print("-------EndExploring-------")
    print("-------startColonysTravel-------")
    env1.startColonysTravel(node = startNode)
    print("-------endColonysTravel-------")

    if NEED_PRINT_TIME_FOR_PROGRAMM_WORK:
        print("----TIME FOR programm : ", time.time() - tick, " ----")

    print("\n\t----RESULT----\n")
    env1.printResume()
#   env1.showColony()