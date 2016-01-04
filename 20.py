#coding:utf-8

s = 1
for x in xrange(1,101):
	s *= x
print sum(map(int, str(s)))