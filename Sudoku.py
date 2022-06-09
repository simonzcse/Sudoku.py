import copy

def listTo2D(list):
    twoDimensionList = [[0 for row in range(9)] for col in range(9)]
    for i in range(len(list)):
        for j in range(len(list[i])):
            for k in range(len(list[i][j])):
                twoDimensionList[i //len(list[i]) * len(list[i][j]) + j][i % len(list[i]) * len(list[i][j]) + k] = list[i][j][k]
    return twoDimensionList

def filePicking():
    return input("Please enter a filename: ")

def simplePrint(list):
    twoDList = listTo2D(list)
    for row in range(9):
        for col in range(9):
            print(' ' if twoDList[row][col] == 0 else chr(twoDList[row][col] + ord('0')), end = '')
        print("")    

def loadCells(cells, filename):
    try:
        f = open(filename, "r")
        line = 0
        for x in f:
            if (line >= 9):
                raise Exception("Incorrect number of lines")
            txt = x.replace('\n', '')    
            if (len(txt) != 9):
                raise Exception("Incorrect number of characters")
            for i in range(9):
                cells[(line // 3) * 3 + i // 3][line % 3][i % 3] = ord(txt[i]) - ord('0')
            line += 1
    except:
        print("Error in reading file :")
        return False
    else:
        return True               


cells= [[ [0 for col in range(3)] for col in range(3)] for row in range(9)]
if (loadCells(cells, filePicking()) == False):
    print("The file is not loaded successfully. You may want to check your filePicking method " +
                                "or see if the file is really placed properly in your project directory.")
    cells[0] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cells[4] = [[1, 0, 3], [4, 5, 6], [0, 8, 9]]
    cells[8] = [[4, 0, 3], [1, 5, 6], [0, 8, 2]]

#backup the originalCells
originalCells= copy.deepcopy(cells)
simplePrint(cells)



