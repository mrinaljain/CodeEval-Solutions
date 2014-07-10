'''
Created on Jul 2, 2014

@author: Bert
'''
import sys
 
test_cases = open(sys.argv[1], 'r')
 
for test in test_cases:
    strang = test.rstrip().split(",")
    num = int(strang[0])
    p1 = int(strang[1])-1
    p2 = int(strang[2])-1
    sep = list(bin(num))[::-1]
    print str(sep[p1]==sep[p2]).lower()
test_cases.close()