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

def printHelpMenu():
    print("Help Menu:")
    print("------------------")
    print("q\t\tQuit the program")
    print("------------------")
    print("w\t\tMove to upper cell")
    print("------------------")
    print("a\t\tMove to left cell")
    print("------------------")
    print("s\t\tMove to lower cell")
    print("------------------")
    print("d\t\tMove to Right cell")
    print("------------------")
    print("c\t\tGet hits")
    print("------------------")
    print(".\t\tClean current cell")
    print("------------------")
    print("1-9\tInput number into cell")    

def advancePrint(cells, row, col):
    twoDList = listTo2D(cells)
    for i in range(len(twoDList)):
        if (i % 3 == 0):
            print("\u253c", end='')
            for j in range(3):
                print("\t\u2500\t\u2500\t\u2500\t\u253c", end='')
            print("")
        for j in range(len(twoDList[i])):
            if (j % 3 == 0):
                print("\u2502\t", end='')
            if (twoDList[i][j] == 0 and row == i and col == j):
                  print("\u25aa\t", end='')
            elif (twoDList[i][j] == 0):
                print("\u2800\t", end='')
            elif (row == i and col == j):
                c = '\u2080'
                for k in range(twoDList[i][j]):
                   c = chr(ord(c)+1)
                print(c, end='')
                print("\t", end='')
            else:        
                print(str(twoDList[i][j])+"\t", end='')
        print("\u2502")
    print("\u253c")
    for j in range(3):
        print("\t\u2500\t\u2500\t\u2500\t\u253c", end='')
    print("")    



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
row = 0
col = 0
advancePrint(cells, row, col)
command = '0'
while True:
    command==input("")
    match command: #Match case is available since Python 3.10, like switch case in java:) 
        case 'a': col = (col + 8) % 9
        case 's': row = (row + 1) % 9
        case 'w': row = (row + 8) % 9
        case 'd': col = (col + 1) % 9
        case '.': mark(row, col, cells, '0')
        case 'c':
            if (isValid(cells) == False):
                print("The puzzle is invalid!")
            elif (same(cells, originalCells) == False):
                print("This is not the same as the original")
            else:
                print("So far so good!")
        case 'q': exit()
        case 'h': printHelpMenu()           
        case _:
            if (command >= ord('0') and command <= ord('9')): 
                mark(row, col, cells, s)
    advancePrint(cells, row, col)
    if (checkWin(cells) and same(cells, originalCells)):
        print("Yeah! you have solved the puzzle!")
        exit()






