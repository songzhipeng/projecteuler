r = 0
for x in xrange(0,101):
	for y in xrange(0,101):
		r = max(r, sum(map(int,str(x**y))))
print r