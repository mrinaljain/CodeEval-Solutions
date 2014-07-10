'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if test == "": break
    line = test.strip().split(",")
    word = line[0]
    try:
        idx = list(word).index(line[1])
    except ValueError:
        idx = -1
    print idx
test_cases.close()
