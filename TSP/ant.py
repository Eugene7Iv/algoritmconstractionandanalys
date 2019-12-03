class Ant:

    def __init__(self,curNode):
        self.brain = AntBrain(curNode)
        self.brain.keepNode(curNode)

    def step(self, startNode):
        targetNode = self.brain.chooseWay(startNode)

class AntBrain:

    def __init__(self, curNode):
        self.mind = []
        self.wayLength = 0
        self.curNode = curNode

    def chooseWay(self, startNode):
        pass

    def wasAt(self, node):
        res = node in self.mind
        return res

    def keepNode(self, node):
        self.mind.append(node)

    def setWayLength(l):
        self.wayLength = l

    def forget(self):
        self.mind.clear()
        self.wayLength = 0

    def getCurNode(self):
        return self.curNode