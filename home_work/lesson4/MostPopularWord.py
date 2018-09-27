#!usr\bin\python

"""Most popular word"""

__author__ = "JayIvhen"

text = raw_input()
text = text.split(' ')
a = dict.fromkeys(text, 0)

for i in a.iterkeys():
	for j in text:
		if i == j:
			a[i] = a[i] + 1

a_rev = {i:[] for i in a.itervalues()}

for i,j in a_rev.iteritems():
	for k,l in a.iteritems():
		if i == l:
			j.append(k)

max_val = 0
for i in a_rev.iterkeys():
	if max_val < i:
		max_val = i

if len(a_rev[max_val]) == 1:
	print a_rev[max_val][0]
else:
	print '---'
