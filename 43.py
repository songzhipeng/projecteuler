# coding: utf-8

import itertools, string
list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = list(itertools.permutations(list1,len(list1)))
res = 0
for lst in list2:
	if lst[0] == 0:
		continue
	if lst[3]%2 != 0:
		continue
	if (lst[2] + lst[3] + lst[4]) % 3 != 0:
		continue
	if lst[5] != 0 and lst[5] != 5:
		continue
	s = string.join(map(str,lst),'')
	if int(s[4:7])%7 != 0:
		continue
	if int(s[5:8])%11 != 0:
		continue
	if int(s[6:9])%13 != 0:
		continue
	if int(s[7:10])%17 != 0:
		continue
	res += int(s)
print res
