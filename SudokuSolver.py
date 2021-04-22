#file = open("testing.txt", "w")
#file.close()
import numpy

def WriteBoard(puzzle):
    file = open("testing.txt", "w")

    tester = ""
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            tester += str(puzzle[i][j])
            if ((j + 1) % 3 == 0 and j != 8):
                tester += " | "
        tester +="\n"
        if ((i + 1) % 3 == 0 and i != 8):
            tester += "---------------\n"

    file.write(tester)
    file.close()

def EmptyBoard():
    puzzle = []
    tempStore = []

    for x in range(9):
        tempStore.clear()

        for y in range(9):
            tempStore.append(0)
        
        puzzle.append(tempStore)

    return puzzle

def Main():
    #Main function here
    puzzle = EmptyBoard()
    puzzle2 = puzzle[2].copy()
    puzzle2.insert(0, 2)
    print(puzzle2)
    print(puzzle)
    puzzle[2] = puzzle2
    WriteBoard(puzzle)
    return 0

Main()