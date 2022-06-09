from array import *

def loadCells(cells, filename):
    f = open(filename, "r")
    for x in f:
        print(x)


cells= [[ [0 for col in range(3)] for col in range(3)] for row in range(9)]
print(len(cells[0][0]))