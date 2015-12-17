# question 4

def isPalindromicNumber(Num):
	num = str(Num)
	size = len(num)
	for i in range(size//2):
		if num[i] != num[-i-1]:
			return False
	return True

val_max = 0
x = 0
y = 0
for i in range(999,100, -1):
	for j in range(999,100, -1):
		if (isPalindromicNumber(i*j) and i*j > val_max):
			val_max = i*j
			x = i
			y = j
print x, y, val_max