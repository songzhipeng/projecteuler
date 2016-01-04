#coding:utf-8

#206

import math

def f(a):
	return int('1%d2%d3%d4%d5%d6%d7%d8%d9%d0'%(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]))

# print len(str(f([0]*9)))
# print int(math.sqrt(f([0]*9))**2) 
# print f([0]*9)

'''
1_2_3_4_5_6_7_8_9_0
1_2_3_4_5_6_7_8_900
1_2_3_4_5_6_7_8_9
x^2=1a2b3c4d5e6f7g8h9i0
x=ABCDEFGHI
i===0
h%2===0
x===10(8k+1)
h为偶数
x/10===3或7
'''

#min:1010101010
#max:1389026623

# a=1929394959697989900
# print a**2
# print math.sqrt(1020304050607080900)
# 1a2b3c4d5e6f7g8h9i0




xxx = (138902663-101010101);
yyy = int(xxx / 100);

for x in xrange(101010101,138902663):
	if (x-101010101)%(yyy)==0:
		print (x-101010101)/yyy,'%'
	if x%10!=3 and x%10!=7:
		continue
	n = x**2
	s = str(n)
	if len(s) == 17:
		if s[0]=='1' and s[2]=='2' and s[4]=='3' and s[6]=='4' and s[8]=='5' and s[10]=='6' and s[12]=='7' and s[14]=='8' and s[16]=='9':
			print x*10, n*100
			break