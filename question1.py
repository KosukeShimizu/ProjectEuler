# question 1

def DivisibleSum(tar, n):
	div = tar // n
	return	sum(range(div + 1)) * n

tar = 999
total = DivisibleSum(tar, 3) + DivisibleSum(tar, 5) - DivisibleSum(tar, 15)
print('Question 1: ' + str(total))