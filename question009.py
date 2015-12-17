# question 9

product = 0
for i in range(1, 1000/2):
	for j in range(1, (1000-i)/2):
		if i**2 + j**2 == (1000-i-j)**2:
			product = i*j*(1000-i-j)

print product