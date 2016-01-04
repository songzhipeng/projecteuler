def f1(n):
	return n*n
print f1(sum(range(1,101))) - sum([f1(x) for x in xrange(1,101)])