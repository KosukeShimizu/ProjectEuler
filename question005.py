# question 5

from math import *

def prime(N):
	primes = [2]
	n = 1
	while(len(primes)<N):
		n += 2
		m = int(sqrt(n))
		for p in primes:
			if p > m:
				primes.append(n)
				break
			if n%p == 0:
				break
	return primes[-1]

def factors(Num):
	factors = []
	N = 1
	i = 0
	while(Num != 1):
		p = prime(N)
		factors.append([p,0])
		while(Num%p == 0):
			factors[i][1] += 1
			Num = Num/p
		N += 1
		i += 1
	return factors

all_factors = []
for i in range(1, 21, 1):
	temp = factors(i)
	for j in range(len(temp)):
		try:
			if j > len(all_factors):
				all_factors.append(temp[j])
			else:
				all_factors[j][1] = max([all_factors[j][1], temp[j][1]])
		except IndexError:
			all_factors.append(temp[j])

val = 1
for i in range(len(all_factors)):
	val *= pow(all_factors[i][0], all_factors[i][1])
print val