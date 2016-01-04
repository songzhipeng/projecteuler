def gcd(a,b):
	return gcd(b,a%b) if b else a
def lcm(a,b):
	return a*b/gcd(a,b)

res = 2520
for x in xrange(11,21):
	res = lcm(res, x)
print res