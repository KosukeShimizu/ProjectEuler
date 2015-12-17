# question 6

tar = 100
ans = sum(range(1, tar+1))**2
for i in range(1, tar+1):
	ans -= i**2

print('Question 6: ' + str(ans))