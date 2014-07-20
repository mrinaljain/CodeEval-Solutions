'''
Created on Jul 2, 2014

@author: Bert
'''

def palindrome(n):
    a = list(str(n))
    b = a[::-1]
    for i in xrange(len(a)):
        if a[i] != b[i]: return False
    return True

import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip()
    num = int(line)
    numlist = list(line)
    niter = 0
        
    while not palindrome(num):
        a = list(str(num))
        b = a[::-1]
        bnum = int(''.join(n for n in b)) 
        num = num + bnum
        niter += 1
    print niter,num
    
test_cases.close()

