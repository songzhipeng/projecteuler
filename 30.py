# coding: utf-8

fac = [0]*10
for x in xrange(0,10):
	fac[x] = x**5

def f(arr):
	return sum([fac[x] for x in arr])
	

res = []
for x in xrange(2,1000000):
	a = map(int, list(str(x)))
	r = f(a)
	if x == r:
		res.append(x)

print res
print sum(res)

