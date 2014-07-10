'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    word = list(test.strip())
    uppers = 0
    for let in word:
        if let.isupper(): uppers+=1
    upPer = float(uppers)/float(len(word))*100
    downPer = 100 - upPer
    print "lowercase: %.2f" % downPer,
    print "uppercase: %.2f" % upPer

test_cases.close()