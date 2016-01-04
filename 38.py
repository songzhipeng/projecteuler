#coding:utf-8

#38

res = 0
for x in xrange(1,10000):
	s = ''
	for y in xrange(1,10):
		s += str(x*y)
		if len(s)>=9:
			break
	if sorted(s) == ['1','2','3','4','5','6','7','8','9']:
		print s
		res = max(res, int(s))
print '>'
print res