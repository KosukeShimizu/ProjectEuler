# question 12

from math import *

def triangleNumber(N):
	return sum(range(1, N+1))

def factors(Num):
	lst = []
	for i in range(1, int(sqrt(Num))+1):
		if Num%i == 0:
			lst.extend([i, Num//i])
	return lst

i = 1
total = 0
while total < 500:
	total = len(factors(triangleNumber(i)))
	i += 1

print triangleNumber(i-1)