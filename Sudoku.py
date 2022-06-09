import copy

# /**
#      * Convert a 3D array to a 9x9 array that is more ready to be printed or to be validated.
#      *
#      * @param array Should be a 3D array where each of the array[i] should be a 3x3 array box.
#      *              There are totally 9 of these array boxes, listed from
#      *              top-left [0], top-middle [1], top-right [2]
#      *              center-left [3], center-middle [4], center-right [5],
#      *              bottom-left [6], bottom-middle [7], bottom-right [8]
#      * @return Returns a 9x9 int array that contains the digits inside the sudoku board. Each of the array[i]
#      *              should contains the number on i-th row, scanned from left to right.
#      */

def listTo2D(list):
    twoDimensionList = [[0 for row in range(9)] for col in range(9)]
    for i in range(len(list)):
        for j in range(len(list[i])):
            for k in range(len(list[i][j])):
                twoDimensionList[i //len(list[i]) * len(list[i][j]) + j][i % len(list[i]) * len(list[i][j]) + k] = list[i][j][k]
    return twoDimensionList

    # /**
    #  * Check if there is any duplicate inside a box Logic
    #  *
    #  * @param cellsOfBox a 3x3 box of a Sudoku. Each cell should contain the number 0 to 9
    #  * @return true if no problem (may not be fully filled up), or false if any one of the number 
    #  *         1 to 9 is repeated inside the box. The number 0, can be repeated.
    #  */

def checkBoxLogic(cellsOfBox):
    count = [0 for i in range(10)]
    for i in range(len(cellsOfBox)):
        for j in range(len(cellsOfBox[i])):
            match cellsOfBox[i][j]:
                case 1:
                    count[1]+=1
                case 2:
                    count[2]+=1
                case 3:
                    count[3]+=1
                case 4:
                    count[4]+=1
                case 5:
                    count[5]+=1
                case 6:
                    count[6]+=1
                case 7:
                    count[7]+=1
                case 8:
                    count[8]+=1
                case 9:
                    count[9]+=1
                case 0:
                    count[0]+=1
    for i in range(1, len(count)):
        if (count[i] >1):
            return False
    return True 
    
    # /**
    #  * Check if there is any duplicate on a line.
    #  *
    #  * @param cellsOfLine an array that contains 9 cells which may contain the number 0 to 9.
    #  * @return true if no problem (may not be fully filled up), or false if any one of the number 
    #  *         1 to 9 is repeated on the line. The number 0, can be repeated.
    #  */
def checkLineLogic(cellsOfLine):
    count = [0 for i in range(10)]
    for i in cellsOfLine:
        match i:
            case 1:
                count[1]+=1
            case 2:
                count[2]+=1
            case 3:
                count[3]+=1
            case 4:
                count[4]+=1
            case 5:
                count[5]+=1
            case 6:
                count[6]+=1
            case 7:
                count[7]+=1
            case 8:
                count[8]+=1
            case 9:
                count[9]+=1
            case 0:
                count[0]+=1
    for i in range(1, len(count)):
        if (count[i] >1):
            return False
    return True     

    # /**
    #  * Check problems of the entire grid
    #  * @param cells 3D array that being checked.
    #  * @return true if no problem (not need to be fully filled)
    #  */
    
def isValid(cells):
    twoDList = listTo2D(cells)
    for ints in twoDList:
        if (checkLineLogic(ints) == False):
            return False
    for sudoku in cells:
        if (checkBoxLogic(sudoku) == False):
            return False
    return True

    # /**
    #  * Check if the sudoku completes
    #  * @param cells 3D array that being checked.
    #  * @return true if the sudoku puzzle is completely filled and valid, 
    #  *         false if otherwise.
    #  */
def checkWin(cells):
    if (isValid(cells) == False):
        return False
    else:
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                for k in range(len(cells[i][j])):
                    if (cells[i][j][k] == 0):
                        return False
        return True 

    # /**
    #  * This method should prompt the user to enter a filename and accept the user's input.
    #  * It is possible that the user input an invalid filename or the there isn't such filename.
    #  * This method does not valid the user's inputs.
    #  *
    #  * @return a filename picked by user.
    #  */
def filePicking():
    return input("Please enter a filename: ")

    # /**
    #  * Print the Help Menu. Please try to understand the switch case in runOnce and 
    #  * Provide a one line comment about the purpose of each symbol.
    #  */
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

    # /**
    #  * To print the Sudoku in a nicer looking way. All horizontal borders should be printed with the char \u2500. All vertical border should
    #  * be printed with the char \u2502. All cross-point should be printed with the symbol \u253c. The highlighted cell, (at the position indicated by row and col),
    #  * should be \u25aa if it is empty or should be \u2081, \u2082,..., \u2089 depends on the value of that cell. Please refer to the sample program
    #  * and see how the program should work.
    #  *
    #  * @param cells 3D cells that is going to be printed.
    #  * @param row the row of where the highlighted cell is.
    #  * @param col the col of where the highlighted cell is.
    #  */
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

    # /**
    #  * To write a number into the sudoku 3D array with the given row, col and char s.
    #  *
    #  * @param row indicate which row (0-8) that the cells is going to be marked
    #  * @param col indicates which col (0-8) that the cells is going to be marked
    #  * @param cells the 3D array that is going to be marked.
    #  * @param s a number '0' to '9'
    #  */
def mark(row, col, cells, s):
    try:
        cells[(row // 3 * 3) + col //3][row % 3][col % 3] = int(s)
    except:
        return    

#    /**
#      * To compare if the original cells are kept in the cells
#      *
#      * For example, cell 1 1 in original cell is 5. This number should not be overwritten by
#      * the player during the game. Otherwise the player can win the game easily. This method
#      * simply check if the givens cells in the original cells are preserved.
#      *
#      * @param cells the cells to be checked
#      * @param originals the original cells
#      * @return true if the number in original cells is kept in cells.
#      */
def same(cells, originals):
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            for k in range(len(cells[i][j])):
                if (originals[i][j][k] != 0 and originals[i][j][k] != cells[i][j][k]):
                    return False
    return True                

    # /**
    #  * The implementation of this method is given. It is completed. This methods calls another method arrayTo2D.
    #  * You need to implement arrayTo2D.
    #  *
    #  * @param array A 3D array where each of the array[i] is a box of 3x3 sudoku.
    #  */
def simplePrint(list):
    twoDList = listTo2D(list)
    for row in range(9):
        for col in range(9):
            print(' ' if twoDList[row][col] == 0 else chr(twoDList[row][col] + ord('0')), end = '')
        print("")    


    # /**
    #  * This method is given. This method is finished.
    #  *
    #  * Load a cells from a file. Each file should contain 9 lines of 9 digits.
    #  * An empty cell will be notated by a 0
    #  * @param cells after reading the digits, the 2D int array should store the sudoku puzzle from the file
    #  * @param filename the filename should be pointed to a file stored under the project directory
    #  *
    #  * @return return true if file read successfully, false if other wise (e.g. in correct number of character per line, insufficient number of lines etc...
    #  */
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

#main
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
command = input()
while True:
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
            if (ord(command) >= ord('0') and ord(command) <= ord('9')): 
                mark(row, col, cells, command)
    advancePrint(cells, row, col)
    if (checkWin(cells) and same(cells, originalCells)):
        print("Yeah! you have solved the puzzle!")
        exit()
    command = input()    
