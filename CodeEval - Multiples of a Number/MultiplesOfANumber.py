'''
Created on Jul 2, 2014

@author: Bert
'''
import sys
 
test_cases = open(sys.argv[1], 'r')
 
for test in test_cases:
    strang = test.rstrip().split(",")
    x = int(strang[0])
    n = int(strang[1])
    z = 0
    while n*z <= x:
        z=z+1
    print n*z
test_cases.close()