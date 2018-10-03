#!usr/bin/python

"""test script

l8 tasks are about importing modules
so we will import here

"""

import cmp_mod

C = cmp_mod.Comparator(123)
class Test: pass
T = Test()
T.value = 124
print C.compare(T)

