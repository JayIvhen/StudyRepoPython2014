#!usr\bin\python

"""Payed stairs"""

# Dinamic programing training
# Each stair have its own price to get on it
# Need to find the lowerest price to achive last stair


__author__ = "JayIvhen"

def u_input():
    while True:
        try:
            stairs = [0] + raw_input("Enter stairs values: ").split(",")
            for i in xrange(len(stairs)):
                stairs[i] = int(stairs[i])
            print stairs
        except ValueError as inst:
            print inst
        else:
            break
    while True:
        try:
            step = int(raw_input("Enter step: "))
            print step
        except ValueError as inst:
            print inst
        else:
            break
    return stairs, step


def brain(stairs, step):
    try:
        for i in xrange(step + 1, len(stairs)):
            stairs[i] = stairs[i] + min(stairs[i - step: i])
    except ValueError as inst:
        print inst
        return "Error"
    return stairs[len(stairs) - 1]


def main():
    print brain(*u_input())


main()
