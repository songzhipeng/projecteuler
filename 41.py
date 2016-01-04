primes = [2,3]
num = 10000000
for i in xrange(5,num):
	flag = True
	for j in primes:
		if j*j>i:
			break
		if i%j==0:
			flag = False
			break
	if flag:
		primes.append(i)


# print len(primes)

def f(a):
	b = list(str(a))
	b.sort()
	c = map(int, b)
	return c


res = 0
for p in primes[::-1]:
	if p < 1000000:
		break
	r = f(p)
	if r == [1,2,3,4,5,6,7]:
		res = max(res, p)
print res

