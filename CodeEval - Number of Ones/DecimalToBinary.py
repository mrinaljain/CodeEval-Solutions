'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    num = int(test.strip())
    num = bin(num)[2:]
    ans = 0
    
    for n in list(str(num)):
        if n == '1': ans += 1
    print ans

test_cases.close()