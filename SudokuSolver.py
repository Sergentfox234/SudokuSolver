#file = open("testing.txt", "w")
#file.close()

def WriteBoard():
    file = open("testing.txt", "w")

    puzzle = []
    tempStore = []

    for x in range(9):
        tempStore.clear()

        for y in range(9):
            tempStore.append(0)
        
        puzzle.append(tempStore)

    tester = ""
    for i in range(9):
        for j in range(9):
            tester += str(puzzle[i][j])
            if ((j + 1) % 3 == 0 and j != 8):
                tester += " | "
        tester +="\n"
        if ((i + 1) % 3 == 0 and i != 8):
            tester += "---------------\n"

    file.write(tester)
    file.close()
    return puzzle

def Main():
    #Main function here
    puzzle = WriteBoard()
    print(puzzle)
    return 0

Main()