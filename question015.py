# question 15

def matrix(col, row):
	mat = []
	for i in range(col):
		mat.append([])
		for j in range(row):
			mat[i].extend([0])
	return mat

def routes(col, row):
	grid = matrix(col+1, row+1)
	for i in range(col+1):
		for j in range(row+1):
			top, left = 0, 0
			if i > 0:
				top = grid[i-1][j]
			if j > 0:
				left = grid[i][j-1]
			if i == 0 and j == 0:
				grid[i][j] = 1
			else:
				grid[i][j] = top + left
	return grid[col][row]

print routes(20,20)