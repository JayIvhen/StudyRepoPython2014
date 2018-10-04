#!usr/bin/python

"""Simple vector.

Lectur page link: http://uneex.ru/LecturesCMC/PythonIntro2014/08_ModulesAndClasses

Lecture 8 Task 3
definr class Dot
    define dor in n-dimetion
    __str__
    find distance between 2 points
    find middle
    if n of dimentions for 2 points is not equal raise ValueError

test script:
   1 for A,B in (mod.Dot(1,2,3),mod.Dot(3,4,5)), (mod.Dot(1,2),mod.Dot(3)):
   2   print A
   3   try:
   4     print "{:.3f}".format(A.distance(B))
   5     print A.middle(B)
   6   except ValueError:
   7     print "ERROR"


output:
    1,2,3
    3.464
    2.0,3.0,4.0
    1,2
    ERROR

"""

from math import sqrt

class Dot:

    def __init__(self, *coord):
        self.coord = coord

    def __str__(self):
        return ",".join(str(i) for i in self.coord)

    def distance(self, other):
        if len(self.coord) != len(other.coord):
            raise ValueError
        elif type(other) == str:
            raise ValueError
        else:
            return sqrt(sum(map(lambda coord: (coord[1]-coord[0])**2,
                                zip(self.coord, other.coord)
                               )
                           )
                       )

    def middle(self, other):
        if len(self.coord) != len(other.coord):
            raise ValueError
        elif type(other) == str:
            raise ValueError
        else:
            return Dot(*map(lambda coord: (coord[0]+coord[1])/2.0,
                           zip(self.coord, other.coord)
                          )
                      )

