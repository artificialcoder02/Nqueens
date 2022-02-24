#Python Code to solve N queens prblem using Backtrcking recursive fucntion
N = 4

#Function for storing the negative indices while shifitng of row-col+N-1 (N-1)
ld = [0] * 30

#To check if the queen can be placed in diagonal or not.
rd = [0] * 30

#Coloumn  Array
cl = [0] * 30

#Utlility Fucntion to print the solution
def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()

 
def solveNQUtil(board, col):

	if (col >= N):
		return True

	for i in range(N):
		
		if ((ld[i - col + N - 1] != 1 and
			rd[i + col] != 1) and cl[i] != 1):
				
		
			board[i][col] = 1
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
			
			if (solveNQUtil(board, col + 1)):
				return True
				
			board[i][col] = 0 # BACKTRACK
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
			
	return False
	

def solveNQ():
	board = [[0, 0, 0, 0,],
			 [0, 0, 0, 0],
			 [0, 0, 0, 0],
			 [0, 0, 0, 0]]

	if (solveNQUtil(board, 0) == False):
		print("NO SOLUTION!")
		return False
	printSolution(board)
	return True
	
# THE MAIN FUNCTION

#The position of the Queens will be presented by 1 in the grid.
solveNQ()


