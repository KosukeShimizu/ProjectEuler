# question 2

seq = [1]
val = 2
sum = 0
while(val <= 4000000):
	prev = seq[-1]
	seq.append(val)
	if not (val%2):
		sum += val
	val += prev

print('Question 2: ' + str(sum))