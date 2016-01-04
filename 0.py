# coding: utf-8

R = dict()
def f(n):
	if n%2 == 0:
		return n/2
	else:
		return n*3+1


def g(n,x):
	# print 'g(',n,',',x,')'
	if n == 1:
		return x
	# elif R.has_key(n):
	# 	print '> R['+str(n)+']=',R[n]
	# 	return x+R[n]
	else:
		return g(f(n),x+1)


def h(n):
	return g(n, 1)

for x in xrange(1,1000001):
	if x % 10000 == 0:
		print x / 10000,'%'
	R[x] = h(x)

# for x in xrange(1,14):
	# print '>>',x
	# R[x] = h(x)
	# print '>>',x,R[x]
	# print '>>>',R



maxValue = max(R.values())
for k in R:
	v = R[k]
	if v == maxValue:
		print k
# print k, R[k]




# print h(13)
# print R[13]


