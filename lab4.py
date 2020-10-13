"""
lab4.py

Isaac AshLind ia378@nau.edu
Lucas Gerosa 

Description: 
Lights Out game for the command line
"""

import random


# Generate a 5 X 5 table
def createTable():
    table = [[], [], [], [], []]
    for row in table:
        for i in range(5):
            row.append(0)
    # Simulate gameplay to randomly populate board with "lights"
    for i in range(25):
        row = random.randint(0, 4)
        column = random.randint(0, 4)
        gameRules(row, column, table)
    return table


# Display the game board
def gameBoard(table):
    print('  A B C D E')
    rowNumber = 1
    for row in table:
        print(rowNumber, end=' ')
        rowNumber += 1
        for i in range(5):
            if row[i] == 0:
                print("\N{WHITE SQUARE}", end=' ')
            else:
                print("\N{BLACK SQUARE}", end=' ')
        print()


# Will flip color of squares to the opposite color
def gameRules(row, column, table):
    def flipValue(row, column):
        value = table[row][column]
        if value == 0:
            value = 1
        elif value == 1:
            value = 0
        table[row][column] = value

    # test for boundaries
    flipValue(row, column)
    if row != 0:
        flipValue(row - 1, column)
    if column != 0:
        flipValue(row, column - 1)
    if column != 4:
        flipValue(row, column + 1)
    if row != 4:
        flipValue(row + 1, column)


def getInputFromUser():
    inputMessage = "\nPlease choose a row (1–5) and column (A–E) (Example: 1A)\n"
    while True:
        inputFromUser = input(inputMessage)
        if inputFromUser.lower == 'quit':
            print("Quitting game")
            return False
        elif len(inputFromUser) != 2:
            print("\nNon-valid input (must choose 1–5 and A–E)")
            continue
        else:
            input0 = inputFromUser[0]
            input1 = inputFromUser[1]
        if (input0 in "12345") and (input1.lower() in "abcde"):
            row = int(input0) - 1
            column = ord(input1) - 97  #converts letters into 0–4
            pass
        # Let's the user input column and row in reverse order
        elif (input0.lower() in "abcde") and (input1 in "12345"):
            row = int(input1) - 1
            column = ord(input0) - 97
            pass
        else:
            print("\nNon-valid input (must choose 1–5 and A–E)")
            continue
        return row, column


def isComplete(table):
    for row in table:
        for i in row:
            if i == 1:
                return False
    return True


def main():
    userInput = input("Press ENTER to start game; type quit to exit.\n— ")
    if userInput.lower() == 'quit':
        print("You exited the game.")
        return
    table = createTable()
    gameBoard(table)
    numberMoves = 0
    while not isComplete(table):
        inputFromUser = getInputFromUser()
        if inputFromUser:
            row, column = inputFromUser
            gameRules(row, column, table)
            gameBoard(table)
            numberMoves += 1

    print(f"Congratulations! You won the game in {numberMoves} moves!")
    input("Press ENTER to quit")


if __name__ == '__main__':
    main()
