import math

primes = [x for x in xrange ( 1 , 775147 ) if not [y for y in xrange ( 2 ,int(math.sqrt(x))+1)   if x % y == 0 ]] 


length = len(primes)
for x in xrange(length-1,-1,-1):
	p = primes[x]
	if 600851475143 % p == 0:
		print p
		break
