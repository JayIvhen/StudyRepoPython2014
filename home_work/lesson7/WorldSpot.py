from __future__ import print_function
# vim: set fileencoding= UTF-8
#!usr/bin/python



"""Word Spot

ENG: Enter string. Output. All world in order they came in, if any word have appired more then once, print index in (paranthesise)

input: qwe sdf tyu qwe sdf try sdf qwe sdf rty sdf wer sdf wer
output:qwe(7) sdf(12) tyu try rty wer(13)

lecture 7 task 3.
http://uneex.ru/LecturesCMC/PythonIntro2014/07_LanguageExtensions

"""

__author__ = "JayIvhen"


from collections import OrderedDict



words_dict = OrderedDict()
words = raw_input().strip(" ").split(" ")

# add words in dict as keys and if it already added add its index. Otherwise add 0
for index in xrange(len(words)):
    if words_dict.has_key(words[index]):
        words_dict[words[index]] = index 
    else:
        words_dict[words[index]] = 0

# Print words in order they came in. if value = 0 print just word, otherwise print word(index, when last seen in text)
for index in words_dict:
    if words_dict[index]:
        print("{}({})".format(index, words_dict[index]), end=' ')
    else:
        print(index, end=' ')
print()
