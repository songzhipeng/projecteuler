def revert(s):
	return s[::-1]

res = 0
for i in xrange(100,1000):
	for j in xrange(100,1000):
		p = i * j
		s = str(p)
		if s == revert(s):
			if p > res:
				res = p


print res