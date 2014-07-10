'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(' ')
    lw = line[0]
    for word in line:
        if len(word) > len(lw):
            lw = word
    print lw
test_cases.close()