'''
Created on Jul 2, 2014

@author: Bert
'''
import sys
 
test_cases = open(sys.argv[1], 'r')
 
for test in test_cases:
    print sum(list(map(int, test.rstrip())))
test_cases.close()