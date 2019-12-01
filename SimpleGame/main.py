import gp

#rf = gp.getrankfunction(gp.buildhiddenset())
#points = [[26,35,829],[8,24,141],[20,1,467],[33,11,1215],[37,16,1517]]
#rf = gp.getrankfunction(points)
#gp.evolve(2, 500, rf, mutationrate=0.2, breedingrate=0.1,pexp=0.7,pnew=0.1)
#p1=gp.makerandomtree(5)
#p2=gp.makerandomtree(5)
#r = gp.gridgame([p1,p2])
#print(r)
winner = gp.evolve(5,500,gp.tournament,maxgen=5000)
gp.gridgame([winner,gp.humanplayer()])