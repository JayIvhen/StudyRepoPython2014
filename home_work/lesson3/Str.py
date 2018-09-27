#!usr/bin/python

"""Repeped strings"""

__author__ = "JayIvhen"


while True:
	a = raw_input('Enter sring: ')
	if type('str') == type(a):
		break
	else:
		raw_input('Input must be STR type: ')
for i in xrange(1, len(a)):
	s = a[0:i]
	k = len(a) / len(s)
	if a == (s * k):
		print 'string= ', a, 's= ', s, 'k= ', k
		break
else:
	print 'NO any repeatble substring'
 
