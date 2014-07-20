'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(';')
    nums = line[0].split(',')
    n = int(line[1])
    ans = []
    
    for i in xrange(0, len(nums), n):
        temp = nums[i:i+n]
        if len(temp) == n: temp.reverse()
        for x in temp: ans.append(x)
    print ','.join(s for s in ans)
    
test_cases.close()