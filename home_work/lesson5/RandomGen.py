#!usr\bin\python

"""Random gen"""

#write a random generator Xn+1=(a*Xn+c) mod m

__author__ = "JayIvhen"

class Data(object):
    def __init__(self, x0 = 0, a = 0, c = 0, m = 0, number = 0):
        self.x0 = x0
        self.a = a
        self.c = c
        self.m = m
        self.Xn = x0
        self.number = number

class U_Error(Exception):
    def __str__(self):
        return "ERROR, try count more then m!"


def u_input():
# reading from input and returning vars as data class

    x0, a, c, m = input()
    number = input()
    return Data(x0, a, c, m, number)

def main():
# main function geting data from input, then looping over algorithm generator
# untill find num or random oblect will be none
    data = u_input()
    try:
        for num in u_random(data):
            print num
            if num == data.number:
                print "YES"
                break
        else:
            print "NO"
#    except Exception:
#        print 'StopIteration'
#    try:
#        for i in xrange(10):
#            pass
#    except :
#        print "EXCEPTION"

def u_random(data):
#algorithm generator "lineyniy conoguentniy generetor sluchaynih"
#cikle leght always < then M. so we will find m == num, or it will be stop iteration
        for i in xrange(data.m):
            data.Xn = ((data.a * data.Xn) + data.c) % data.m
            yield data.Xn



main()


