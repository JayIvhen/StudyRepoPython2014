#!usr\bin\python

"""SubModule counter"""

#count how many objects of module are modules themselfs

__author__ = "JayIvhen"

def u_input():
    pass

def u_count(name):
    a = 0
    try:
        module =  __import__(name)
        for i in dir(module):
            try:
                print i,
                print type(eval('module' + '.{}'.format(i)))
                if "module" in str(type(eval('module' + '.{}'.format(i)))):
                    print "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
                    a = a + 1
#                __import__(name + '.{}'.format(i))
#                a = a + 1
#                print 'ok OK ok OK ok OK ok OK ok OK ok OK ok OK ok OK ok OK ok OK ok OK ok OK ok OK ok OK ok'
            except ImportError:
                pass
    except ImportError, NameError:
        print -1
    else:
        print a
