primes = [2,3]
num = 1000000
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
print primes[10000]