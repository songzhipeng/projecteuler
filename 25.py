# coding: utf-8

fac = [1,1]
for x in xrange(2,100000):
	fac.append(fac[x-1]+fac[x-2])
	if len(str(fac[x])) >= 1000:
		print x+1
		break