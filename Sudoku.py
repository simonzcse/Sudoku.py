def filePicking():
    return input("Please enter a filename: ")


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
                                "or see if the file is really placed properly in your project directory.\n")
    cells[0] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cells[4] = [[1, 0, 3], [4, 5, 6], [0, 8, 9]]
    cells[8] = [[4, 0, 3], [1, 5, 6], [0, 8, 2]]
originalCells= [[ [0 for col in range(3)] for col in range(3)] for row in range(9)]                              