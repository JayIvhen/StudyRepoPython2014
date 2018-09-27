#!usr\bin\python

"""String to set"""

__author__ = "JayIvhen"

a = raw_input()
a = a.strip(' ').split(' ')
b = []

for i in a:
	b.append(set(i))

max_len_of_b_item = 0

for i in b:
	if len(i) > max_len_of_b_item:
		max_len_of_b_item = len(i)

for i in xrange(1, max_len_of_b_item+1):
	for j in xrange(len(b)):
		if len(b[j]) == i:
			print a[j],
