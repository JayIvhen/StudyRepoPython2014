#!usr/bin/python
from __future__ import print_function

"""KdigitNbase

Lecture source http://uneex.ru/LecturesCMC/PythonIntro2014/07_LanguageExtensions

Lecture 7 task 1.
Input 2 numbers k,n.
Output all K-degit N-base numbers in collumn.

2,4

10
11
12
13
20
21
22
23
30
31
32
33

"""

__author__ = "JayIvhen"

# stdlib imports
from itertools import takewhile
from itertools import count

# third party imports

# local imports


def main():
    """Main func"""
    nums = input_()
    brain(*nums)


def input_():
    """Input func

    check input. isdegit? is len = 2?
    return list [1,2]

    """
    while True:
        nums = raw_input().split(",")
        if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
            for i in  xrange(len(nums)):
                nums[i] = int(nums[i])
            return nums
        elif nums == "exit":
            return nums
        print("Error, incorrect input. Please reenter")
    

def gen(c, N):
    """ gen func.

    convert decinal representation of Nbased num to, N-basesed represetation

    """
    degit_dict = "0123456789ABCDEF"
    if  c // N == 0:
        return degit_dict[c%N]
    else:
        return gen(c//N, N) + degit_dict[c%N]

def brain(k, N):
    """ Brain func.
    
    prints in colunm all K-degit nums of N-base

    """
    # Generator object which produce n+1 decimal representation of N-based num
    c = count(int(str(10**(k-1)), N), 1)
    # Cicle which generate N-based string represenatation of (c), until len less then K-degit
    for num in takewhile(lambda x: len(x) < k+1, (gen(i, N) for i in c)):
        print(num)


main()
