#!usr/bin/python
  
"""test script

l8 tasks are about importing modules
so we will import here

"""

import PrimitiveDot

for A,B in ((PrimitiveDot.Dot(1,2,3),PrimitiveDot.Dot(3,4,5)),
           (PrimitiveDot.Dot(1,2),PrimitiveDot.Dot(3))):
    print A
    try:
        print "{:.3f}".format(A.distance(B))
        print A.middle(B)
    except ValueError:
        print "ERROR"
