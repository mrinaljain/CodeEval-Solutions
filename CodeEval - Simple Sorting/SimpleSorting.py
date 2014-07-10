'''
Created on Jul 2, 2014

@author: Bert
'''

# import sys
# test_cases = open(sys.argv[1], 'r')
# 
# for test in test_cases:
#     nums = map(float, test.strip().split(" "))
#     print " ".join(str(x) for x in sorted(nums))
# test_cases.close()

import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    nums = sorted(map(float, test.strip().split(" ")))
    for num in nums:
        print '%0.3f' % num,
    print
test_cases.close()