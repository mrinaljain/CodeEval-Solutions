'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    if int(test.strip()) % 2 == 0: print 1
    else: print 0
    
test_cases.close()