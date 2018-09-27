#!usr/bin/python

import math

cX, cY, R = input('Enter circul X,Y,R: ')
a = input('Enter points X,Y: ')
OK_sign = True
i = 0
while i <= (len(a)-1):
	v = math.sqrt((a[i]-cX)**2 + (a[i+1]-cY)**2)
	i = i + 2
	if R == v:
		continue
	OK_sign = False
if OK_sign:
	print('OK') 

