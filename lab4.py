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
	table = [[],[],[],[],[]]
	for row in table:
		for i in range(5):
			row.append(0)
	# Simulate gameplay to randomly populate board with "lights"
	for i in range(25):
		row = random.randint(0, 4)
		column = random.randint(0, 4)
		gameRules(row + 1, column + 1, table)
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
	if type(column) is str:
		if column.lower() in "abcde":
			column = ord(column) - 96 #converts letters into 0–4
		elif column in "12345":
			column = int(column)
		else:
			raise Exception("Non-valid column. (only values 1–5 and A–E are accepted)")
	elif type(column) is int:
		if column > 5 or column < 1:
			raise Exception(f"Non-valid column. (only values 1–5 and A–E are accepted, and you put in a {column})")
	row = int(row)
	column -= 1 #converts 1–5 to 0–4
	row -= 1
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
		flipValue(row, column -1)
	if column != 4:
		flipValue(row, column + 1)
	if row != 4:    
		flipValue(row + 1, column)


def getInputFromUser():
	inputMessage = "\nPlease choose a row (1–5) and column (A–E) (Example: 1A)."
	inputFromUser = input(inputMessage)
	if inputFromUser == 'QUIT':
			print("Quitting function.")
			return False
	else:
		row = inputFromUser[0]
		column = inputFromUser[1]
		return row, column

def main():
	userInput = input("Press ENTER to start game; type quit to exit.\n— ")
	if userInput.lower() == 'quit':
		print("You exited the game.")
		return
	table = createTable()
	gameBoard(table)
	while True:
		inputFromUser = getInputFromUser()
		if inputFromUser:
			row, column = inputFromUser
			gameRules(row, column, table)
			gameBoard(table)
		else:
			return

if __name__ == '__main__':
	main()
