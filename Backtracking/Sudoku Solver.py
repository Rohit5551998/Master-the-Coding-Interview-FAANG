import math

def solveSudoku(board):
	n = len(board)
	boxes = [0 for i in range(n)]
	rows = [0 for i in range(n)]
	cols = [0 for i in range(n)]

	for i in range(n):
		boxes[i] = {}
		rows[i] = {}
		cols[i] = {}

	for r in range(n):
		for c in range(n):
			if(board[r][c] != '.'):
				val = board[r][c]
				boxId = getBoxId(r, c)
				boxes[boxId][val] = True
				rows[r][val] = True
				cols[c][val] = True

	solveBacktrack(board, boxes, rows, cols, 0, 0)

def isValid(box, row, col, num):
	if(box[num] or row[num] or col[num]):
		return False
	else:
		return True

def getBoxId(row, col):
	rowVal = math.floor(row/3)*3
	colVal = math.floor(col/3)
	return rowVal + colVal

def solveBacktrack(board, boxes, rows, cols, r, c):
	if (r == len(board) or c == len(board[0])):
		return True
	
	else:
		if(board[r][c] == '.'):
			for num in range(1, 10):
				numVal = str(num)
				board[r][c] = numVal

				boxId = getBoxId(r, c)
				box = boxes[boxId]
				row = rows[r]
				col = cols[c]

				if(isValid(box, row, col, numVal)):
					box[numVal] = True
					row[numVal] = True
					col[numVal] = True

					if(c == len(board[0]) - 1):
						if(solveBacktrack(board, boxes, rows, cols, r+1, 0)):
							return True

					else:
						if(solveBacktrack(board, boxes, rows, cols, r, c+1)):
							return True 

				del box[numVal]
				del row[numVal]
				del col[numVal]
			
			board[r][c] = "."

		else:
			if(c == len(board[0]) - 1):
				if(solveBacktrack(board, boxes, rows, cols, r+1, 0)):
					return True

			else:
				if(solveBacktrack(board, boxes, rows, cols, r, c+1)):
					return True 

	return False			