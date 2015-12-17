# question 10

from math import *

def PrimeSumBelow(N):
	primes = [2]
	n = 1
	while(primes[-1]<N):
		n += 2
		m = int(sqrt(n))
		for p in primes:
			if p > m:
				primes.append(n)
				break
			if n%p == 0:
				break
	primes.remove(primes[-1])
	return primes

print sum(PrimeSumBelow(2000000))