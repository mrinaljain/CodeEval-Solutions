'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    num = int(test.strip())
    visited = set()
    while 1:
        if num == 1:
            print 1
            break
        num = sum(int(n) ** 2 for n in str(num))
        if num in visited:
            print 0
            break
        visited.add(num)

test_cases.close()