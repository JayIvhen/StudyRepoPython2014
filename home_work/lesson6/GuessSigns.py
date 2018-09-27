from __future__ import print_function
#!usr/python/bin

__author__ = "JayIvhen"

import sys
import os

DEBUG = "DEDUG MESSAGE: "


# Fill expression with signs "+","-","=", print YES if we can place
# them that in way expression will be correct


def u_input():
    """
    User input with checking.
    
    """
    while True:
        try:
            Nums = map(int, (raw_input().split(" ")))
        except ValueError:
            print("Wrong input: ")
        except Exception as inst:
            print(DEBUG, "Something gone wrong", inst, file = sys.stderr)
        else:
            if len(Nums) == 0:
                print("Blank list, enter something: ")
            else:
                break
    return Nums


def expression_possible(Nums, Index, Summ):
    """
    Function will check. Correct or not is expression with Nums
    and "+","-","=" between.
    
    """
    if Index == 0:
        Summ = Nums[0]
        return expression_possible(Nums, Index + 1, Summ)
    for Sign in ["+","-"]:
        try:
            if Sign == "+":
                print(Summ)
                if expression_possible(Nums, Index + 1, Summ + Nums[Index]):
                    return True
            elif Sign == "-":
                print(Summ)
                if expression_possible(Nums, Index + 1, Summ - Nums[Index]):
                    return True
        except IndexError:
            print('summ except', Summ)
            if Summ == 0:
                return True
            else:
                return False
    if Index == (len(Nums) - 1):
        return False


def main():
    """
    Main function. It speakes for itself.

    """
    if expression_possible(u_input(), Index = 0, Summ = 0):
        print("YES")
        print (os.times())
    else:
        print("NO")
        print(os.times())


main()
