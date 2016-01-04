a = 1
b = 2
c = 3
s = 2
while c <= 4000000:
	if c%2 == 0:
		s += c
	a = b
	b = c
	c = a + b
print s