# question 7

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

print('Question 7: ' + str(prime(10001)))