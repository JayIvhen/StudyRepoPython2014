#!usr/bin/python

"""Paralel lines

"""

__author__ = "JayIvhen"

from random import *


def random_points():
	'''This function generates random coord
	
	and also tell us are they paralel
	'''
	random_range_start = -50
	random_range_stop = 100
	a = random_range_start
	b = random_range_stop

	rand_result = randrange(2)
	if rand_result:
		x2_1 = float(randrange(a, b))
		y2_1 = float(randrange(a, b))
		k1 = round((y2_1 / x2_1), 2)
		x1 = float(randrange(a, b))
		y1 = float(randrange(a, b))
		x2 = x2_1 + x1
		y2 = y2_1 + y1
		
		k2 = k1
		x4_3 = float(randrange(a, b))
		y4_3 = k2 * x4_3
		x3 = float(randrange(a, b))
		y3 = float(randrange(a, b))
		x4 = x4_3 + x3
		y4 = y4_3 + y3
		
		paralel = 'YES'
	else:
		x2_1 = float(randrange(a, b))
		y2_1 = float(randrange(a, b))
		k1 = round((y2_1 / x2_1), 2)
		x1 = float(randrange(a, b))
		y1 = float(randrange(a, b))
		x2 = x2_1 + x1
		y2 = y2_1 + y1

		x4_3 = float(randrange(a, b))
		y4_3 = float(randrange(a, b))
		k2 = round((y4_3 / x4_3), 2)
		x3 = float(randrange(a, b))
		y3 = float(randrange(a, b))
		x4 = x4_3 + x3
		y4 = y4_3 + y3

		paralel = 'NO'

	
	print  x1, y1, x2, y2, x3, y3, x4, y4, k1, k2, paralel
	return x1,y1,x2,y2,x3,y3,x4,y4

def paralel(x1,y1,x2,y2,x3,y3,x4,y4):
	'''Function checking are 2 lines paralel or not
	'''
	k1 = round(((y2 - y1) / (x2 - x1)), 2)
	k2 = round(((y4 - y3) / (x4 - x3)), 2)
	if k2 == k1:
		paralel = "YES"
	else:
		paralel = "NO"
	print x1 ,y1 ,x2 ,y2, x3, y3, x4, y4, k1, k2, paralel

remains = 40
while remains:
	remains = remains - 1
	a = random_points()
	print(paralel(*a))
