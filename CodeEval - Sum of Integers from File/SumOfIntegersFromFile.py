'''
Created on Jul 2, 2014

@author: Bert
'''
import sys
 
test_cases = open(sys.argv[1], 'r')

s = 0

for test in test_cases:
    s += int(test)

print s
test_cases.close()