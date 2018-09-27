#!usr/bin/python

"""Construct it"""

# "Construckt It" by ******
# check avalibility of construction Machine from parts
# input                                       [Machine] [Part1] [part2] [ part....]
# if just 1 word string - that is a part      [Part1] 
# We have infinit count of all parts

__author__ = "JayIvhen"

class EndOfInput(Exception):
    "End of user input"
    def __repr__(self):
        return "End of user input"


def u_input():
    "function for reading user input"
    blueprint = []
    while True:
        try:
            string = raw_input()
            if not string:
                raise EndOfInput
            blueprint.append(string.split(' '))
        except EndOfInput:
            break
    print blueprint
    return blueprint


def dinamic(machine):
    print machine
    if (to_do.has_key(machine)) and (machine not in parts):
        if to_do[machine].issubset(parts):
            parts.add(machine)
            print 'c', True
            return True
        a = None
        for part in to_do[machine]:
            b =  dinamic(part)
            if b == True and a != False:
                a = True
            else:
                a = False
        else:
            print 'a',a
            if a:
                return True
            else:
                return False
    elif machine not in parts:
        print 'b', False
        return False
    else:
        print 'b',True
        return True


def brain(blueprint):
    """main work here
    tring to find parts wich we can asemble and adding them to part set"""
    global parts
    parts = set()
    global to_do 
    to_do = dict()
    machine = ''
    for item in blueprint:
        print 'item: ',item
        if len(item) == 1:
            parts.add(item[0])
        else:
            to_do[item[0]] = set(item[1:])
            if item[0][0].isupper():
                machine = item[0]
    if dinamic(machine):
        print "Yes"
    else:
        print "No"
    
#    dict_len_old = len(to_do) + 1
#
#          Old version.
#
#    while dict_len_old != len(to_do):
#        break_flag = 0
#        dict_len_old = len(to_do)
#        for needed_parts in to_do.keys():
#            if to_do[needed_parts].issubset(parts):
#                if needed_parts == machine:
#                    print "YES"
#                    break_flag = 1
#                    break
#                to_do.pop(needed_parts)
#                parts.add(needed_parts)
#        if break_flag == 1:
#            break
#    else:
#        print "NO"


def main():
    "main func - thats all"
    brain(u_input())


main()
