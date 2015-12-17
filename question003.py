# question 3

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

val = 600851475143
p_max = 1
n = 1
while(val != 1):
	p = prime(n)
	while(val%p == 0):
		p_max = p
		val = val//p
	n+=1
print('Question 3: ' + str(p_max))