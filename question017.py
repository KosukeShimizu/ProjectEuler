# question 17

def NumLetters(Num):
	count = 0
	thousandth = Num//1000
	if thousandth >= 1:
		return 11
	hundredth = Num//100
	if hundredth >= 1:
		if hundredth in [1, 2, 6]:
			count += 3
		elif hundredth in [4, 5, 9]:
			count += 4
		elif hundredth in [3, 7, 8]:
			count += 5
		count += 7
	val = Num%100
	if val != 0 and hundredth != 0:
		count += 3
	tenth = val//10
	val = val%10
	if tenth > 0:
		if tenth >= 2:
			if tenth in [4, 5, 6]:
				count += 5
			elif tenth in [2, 3, 8, 9]:
				count += 6
			elif tenth in [7]:
				count += 7
		elif tenth == 1:
			val += 10
	if val in [1, 2, 6, 10]:
		count += 3
	elif val in [4, 5, 9]:
		count += 4
	elif val in [3, 7, 8]:
		count += 5
	elif val in [11, 12]:
		count += 6
	elif val in [15, 16]:
		count += 7
	elif val in [13, 14, 18, 19]:
		count += 8
	elif val in [17]:
		count += 9
	return count

total = 0
for i in range(1, 1001):
	total += NumLetters(i)

print NumLetters(100)
print total