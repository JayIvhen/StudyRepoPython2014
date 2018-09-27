#!usr/bin/python

""" Min Max of function"""


__author__ = "JayIvhen"


from math import *

class Error(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def main(func, coord):
    MinMax = []
    x1, x2 = eval(coord)
    for x in xrange(x1, x2+1):
        try:
            a = eval(func)
            MinMax.append(a)
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
    print min(MinMax),max(MinMax)
    
def input_u():
    while True:
        try:
            func = raw_input()
            coord = raw_input()
            break
        except Exeption:
            print "Incorrect input"
    return func, coord

    
main(*input_u())
