#coding:utf-8

#36

def f(s):
	return s == s[::-1]

res = 0
for x in xrange(1,1000001):
	if f(str(x)) and f(str(bin(x))[2:]):
		print x
		res += x
print '>'
print res