#!usr/bin/python

FirstMax = 0
SecondMax = 0
a = input('Enter object: ')
for j in a:
	if FirstMax < j:
		SecondMax, FirstMax = FirstMax, j
print SecondMax
		

