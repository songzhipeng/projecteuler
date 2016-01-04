for x in xrange(1,1000):
	for y in xrange(x+1,1000):
		z = 1000 - x - y
		if x*x+y*y==z*z:
			print x*y*z