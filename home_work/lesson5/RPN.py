#!usr/bin/python

""" RandomPolishNotation"""

__author__ = "JayIvhen"

from collections import deque

def input():
    while True:
        RPN = []
        input_data = raw_input('Enter RPN: ').split(' ')
        if input_data == 'exit':
#make a correct shutdown
            pass
        count = 0
        for i in input_data:
            try:
                RPN.append(int(i))
            except ValueError as inst:
                if i in ('+','-','/','*'):
                    RPN.append(i)
                else: 
                    print 'wrong sinbol: ', inst
            finally:
                if len(RPN) == len(input_data):
                    break_flag = 1
                else:
                    break_flag = 0
        if break_flag == 1:
            break
    return RPN



def output():
    pass

def brain(RPN):
    RPN = deque(RPN)
    count = []
    while True:
        try:
            if type(RPN[0]) == int:
                count.append(RPN.popleft())
                continue
            else:
                a = eval('count[len(count) - 2] {} count[len(count) - 1]'.format(RPN[0]))
                count[len(count) - 2:len(count)] = [a,]
                RPN.popleft()
        except IndexError:
            break
    return count

def main():
    pass


