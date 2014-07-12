'''
Created on Jul 2, 2014

@author: Bert
'''

import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(' ')
    ans = 0
    indices = [i for i, x in enumerate(line) if x == '"label":']
    for idx in indices:
        ans += int(line[idx-1].strip(','))
    print ans
    
test_cases.close()