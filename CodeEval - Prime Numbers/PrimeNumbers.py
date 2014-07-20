'''
Created on Jul 2, 2014

@author: Bert
'''


import sys
from math import sqrt

test_cases = open(sys.argv[1])

for test in test_cases:
    last = int(test.strip()) + 1
    l = range(2, last)
    t = [True]*len(l)
    nums = dict(zip(l, t))
    ans = []
     
    for i in xrange(2, int(sqrt(last-1))+1):
        if nums[i]:
            for j in xrange(last):
                    if i*i+j*i > last: break
                    nums[i*i+j*i] = False
     
    for key, value in nums.iteritems():
        if value: ans.append(key)
    print ','.join(str(s) for s in ans)
test_cases.close()