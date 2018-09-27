#!usr/bin/python

a = dir(int(input('Enter object: ')))

for b in a:
	if b[0] != '_':
		print b

