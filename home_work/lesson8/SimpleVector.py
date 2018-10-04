#!usr/bin/python

"""Simple vector.

Lectur page link: http://uneex.ru/LecturesCMC/PythonIntro2014/08_ModulesAndClasses

Lecture 8 Task 2
definr class Vector, with following methods:
    define vector
    vector + vector
    vector * vector
    vector * int
    __str__

test script:
   1 A = mod.Vector(1,2)
   2 B = mod.Vector(3,4)
   3 print A
   4 print A+B
   5 print A*B
   6 print 7*A


output:
    |1,2|
    |4,6|
    11
    |7,14|

"""

class Vector:
    
    def __init__(self, *vec):
        self.vec = vec

    def __str__(self):
        return "|{},{}|".format(self.vec[0], self.vec[1])

    def __add__(self, other):
        return Vector(self.vec[0] + other.vec[0],
                      self.vec[1] + other.vec[1]
                     )
    def __mul__(self, other):
        if type(self) == type(other):
            return sum(map(lambda vec: vec[0] * vec[1],
                        zip(self.vec, other.vec)
                       )
                   )
        else:
            return Vector(self.vec[0] * other, self.vec[1] * other)

    __rmul__ = __mul__




