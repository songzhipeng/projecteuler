# coding: utf-8

# print map(int, list(str(123)))

primes = [2,3]
primeDic = dict()
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
for p in primes:
	primeDic[p] = True
# print primes[:100]

result = []


for p in primes[4:]:
	s = str(p)
	if len(s) == 2:
		#两位数
		if primeDic.has_key(int(s[:1])) and primeDic.has_key(int(s[-1:])):
			result.append(p)
	elif len(s) == 3:
		#三位数
		if primeDic.has_key(int(s[:1])) and primeDic.has_key(int(s[-1:])):
			if primeDic.has_key(int(s[:2])) and primeDic.has_key(int(s[-2:])):
				result.append(p)
	elif len(s) == 4:
		#四位数
		if primeDic.has_key(int(s[:1])) and primeDic.has_key(int(s[-1:])):
			if primeDic.has_key(int(s[:2])) and primeDic.has_key(int(s[-2:])):
				if primeDic.has_key(int(s[:3])) and primeDic.has_key(int(s[-3:])):
					result.append(p)
	elif len(s) == 5:
		#五位数
		if primeDic.has_key(int(s[:1])) and primeDic.has_key(int(s[-1:])):
			if primeDic.has_key(int(s[:2])) and primeDic.has_key(int(s[-2:])):
				if primeDic.has_key(int(s[:3])) and primeDic.has_key(int(s[-3:])):
					if primeDic.has_key(int(s[:4])) and primeDic.has_key(int(s[-4:])):
						result.append(p)
	elif len(s) == 6:
		#六位数
		if primeDic.has_key(int(s[:1])) and primeDic.has_key(int(s[-1:])):
			if primeDic.has_key(int(s[:2])) and primeDic.has_key(int(s[-2:])):
				if primeDic.has_key(int(s[:3])) and primeDic.has_key(int(s[-3:])):
					if primeDic.has_key(int(s[:4])) and primeDic.has_key(int(s[-4:])):
						if primeDic.has_key(int(s[:5])) and primeDic.has_key(int(s[-5:])):
							result.append(p)

# print result
print sum(result)
