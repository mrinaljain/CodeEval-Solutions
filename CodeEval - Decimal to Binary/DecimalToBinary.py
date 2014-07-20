'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    num = int(test.strip())
    print bin(num)[2:]

test_cases.close()