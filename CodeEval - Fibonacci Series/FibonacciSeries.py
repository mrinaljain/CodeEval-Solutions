'''
Created on Jul 2, 2014

@author: Bert
'''
# import sys
#  
# def F(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return F(n-1)+F(n-2) 
#  
# test_cases = open(sys.argv[1], 'r')
#  
# for test in test_cases:
#     print F(int(test,))
# test_cases.close()

import sys
from math import sqrt

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    n = int(test.rstrip())
    print int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
test_cases.close()
