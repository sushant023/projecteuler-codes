x = []
y = []
for item in xrange(1,101):
	x.append(item**2)
	y.append(item)
sum1 = 0
sum2 = 0
for num in range(len(x)):
	sum1 += x[num]
	sum2 += y[num]
square = sum2 ** 2
print square - sum1
