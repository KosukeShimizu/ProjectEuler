# question 18

def monthData(yy):
	month_data = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	if yy%4 == 0 and (yy%100 != 0 or yy%400 == 0):
		month_data[2] = 29
	return month_data

days = 1
count = 0
for i in range(1901, 2001):
	month_data = monthData(i)
	for j in range(1, 13):
		days += month_data[j]
		if days%7 == 6:
			count += 1
		days %= 7
print count
