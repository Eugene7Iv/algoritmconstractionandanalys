import random
from environment import *

env1 = Environment()
env1.loadGraphFromTxt("five_d19.txt")
env1.initAntColony(5)
print("-------locateAnt-------")
env1.locateAnt(0)
env1.showColony()
print("-------endlocateAnt-------")
print("-------Exploring-------")
env1.startExploring(10)
print("-------EndExploring-------")
print("-------startColonysTravel-------")
env1.startColonysTravel()
#env1.showColony()