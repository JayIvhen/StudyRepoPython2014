#!usr/bin/python

"""Max substring"""

# MaxSubst.py
# Home_work l6 UNEEX.ru
# Find MaxSubstring with unic letters


__author__ = "JayIvhen"

class blanck_string(Exception):
    def __repr__(self):
        return "String is empty"


def u_input():
    while True: 
        try:
            str = raw_input()
            if len(str) == 0:
                raise blanck_string
        except blanck_string as inst:
            print inst
        except:
            print 'Error'
        else:
            break
    return str


def main():
    print MaxSubSt(u_input())


def MaxSubSt(str):
    max_unic_str_old = ''
    max_unic_str_new = ''
    for i in xrange(len(str)):
        for j in xrange(i, len(str)):
            if str[j] not in max_unic_str_new:
                print "old", max_unic_str_old
                max_unic_str_new = max_unic_str_new + str[j]
                print "new", max_unic_str_new
            else:
                if len(max_unic_str_old) < len(max_unic_str_new):
                    print "old", max_unic_str_old
                    max_unic_str_old = max_unic_str_new
                    print "old new", max_unic_str_old
                    max_unic_str_new = ''
                    print "new new", max_unic_str_new
                    break
                else:
                    max_unic_str_new = ''
                    break
    return max_unic_str_old



