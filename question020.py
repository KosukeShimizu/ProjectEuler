# question 20

def factorials(n):
	product = 1
	for i in range(1, n+1):
		product *= i
	return product

val = list(str(factorials(100)))
total = sum([int(i) for i in val])
print total