#!usr/bin/python

"""
Write decorator wich saves function result between cals.

input:
 def f1(n):
  print 'f1 called'
  return n*n

@mod.function_cachier
def f2(n):
  print 'f2 called'
  return n*n*n

print len([ f1(n) for n in range(3)])
print len([ f1(n) for n in range(3)])
print len([ f2(n) for n in range(4)])
print len([ f2(n) for n in range(4)])

output:
 f1 called
f1 called
f1 called
3
f1 called
f1 called
f1 called
3
f2 called
f2 called
f2 called
f2 called
4
4

"""

"""
save_dict = {}
def function_cachier(func):
    global save_dict
    def wrapper(n, i = 0):
        if n in save_dict.viewkeys():
            return save_dict[n]
        else:
            save_dict[n] = func(n, i)
        return save_dict[n]
    return wrapper
"""
 
def function_cachier(func, *a):
    cashe = dict()
    def wraped(n):
        if n in cashe:
            return cashe[n]
        res = func(n)
        cashe[n] = res
        return res
    return wraped


def f1(n):
    print 'f1 called'
    return n*n

@function_cachier
def f2(n):
    print 'f2 called'
    return n*n*n

f2(2)
print dir()

