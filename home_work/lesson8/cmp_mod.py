#!usr/bin/python

"""Comparator

make class Comparator with fild - value
and method - compare working jast as cmp()


"""

class Comparator():
    def __init__(self, value):
        self.value = value
    def compare(self, other):
        if self.value > other.value:
            return 1
        elif self.value == other.value:
            return 0
        else:
            return -1
