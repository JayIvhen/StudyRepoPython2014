#!usr/bin/python

"""ParamForm

Lecture 7 task 2
Lecture source http://uneex.ru/LecturesCMC/PythonIntro2014/07_LanguageExtensions

input:
    first line. Parametric Formula
    second line. Params with values or ranges

output:
    Max result

input:
Param**2+Fun/6-Result+1
Param=3 Fun=-21,45 Result=5,15
output:
    12

"""
import itertools
import collections


formula = raw_input()
vars_str = raw_input().split(" ")
vars_ = collections.OrderedDict()
print formula
print vars_str
print vars_

for item in vars_str:
    vars_.update([item.split("=")])
print vars_
for item in vars_.iterkeys():
    print 1
    if len(vars_[item]) == 1:
        print 2
        vars_[item] = xrange(int(vars_[item]), int(vars_[item]) + 1)
        print vars_[item]
    else:
        print 3
        vars_[item]= xrange(int(vars_[item].split(',')[0]), int(vars_[item].split(',')[1]) + 1)
        print vars_[item]
    
print vars_
print itertools.product(*list(vars_.itervalues())).next()

max_ = max(map(
           eval("lambda " + "(" +  ", ".join(vars_.iterkeys()) + ")" + ": " + formula),
           itertools.product(*list(vars_.itervalues())))
          )
print max_

