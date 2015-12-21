# question 14

def generator(Num):
	if Num%2 == 0:
		return Num//2
	else:
		return 3 * Num + 1

def totalTerm(ini):
	val = ini
	term = 1
	while val != 1:
		term += 1
		val = generator(val)
	return term

ini = 0
term = 0
for i in range(1, 1000000):
	temp = totalTerm(i)
	if temp > term:
		term = temp
		ini = i

print ini