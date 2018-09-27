#!usr/bin/python

""" summ of 10 nums

if any num is summ of not much then 10 any others print 'YES'

"""

__author__ = "JayIvhen"

from collections import deque

nums = list(input('Enter numbers string: '))
N = input('Enter Number : ')
summ = 0
i = 0
flag = False
iteration_n = 0

def rec_fun(summ, nums, i):
	global flag
	summ = summ + i
	global iteration_n 
	iteration_n += 1
	print 'Itration N', iteration_n
	for j in xrange(len(nums)):
		if N == summ:
			flag = True
		if flag == True:
			return
		else:
			i = nums[j]
			print 'i =', i
			nums_iter = nums[:]
			print 'nums =', nums	
			nums_iter.remove(nums[j])
			print 'nums_iter =', nums_iter
			rec_fun(summ, nums_iter, i)


rec_fun(summ, nums[:], i)
if flag:
	print "YES"
else:
	print "NO"
