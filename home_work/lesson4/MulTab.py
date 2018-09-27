#!usr\bin\python

"""Multiplication Tab"""

__author__ = "JayIvhen"

while True:
	try:
		m, n = input()
	except Exception:
		pass
	try:
		if type(m) == int:
			if type(n) == int:
				break
		raise InvalidOperation
	except Exception:
		print 'Wrong input. Correct input format: (tow integers) m,n'
	
for i in xrange(1,n+1):
	print '{:_>{len1}}_=_{i:_>{len2}}_*_{m}'.format(
		m*i, i = i, m = m, len1 = len(str(m*n)), len2 = len(str(n)))
