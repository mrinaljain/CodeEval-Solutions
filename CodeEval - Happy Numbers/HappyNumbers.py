'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if int(test) == 1: print 1
    else:
        l = list(map(int, test.strip()))
        print l
        s = 0
        for num in l: s += num*num
        l = s
            while s != 1:
                continue
test_cases.close()
