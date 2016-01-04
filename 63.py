# coding: utf-8

result = []
for a in xrange(1,100):
	for b in xrange(1,100):
		c = a**b
		if len(str(c)) == b:
			print a,b
			result.append((a,b))
		elif len(str(c)) > b:
			continue
print len(result)