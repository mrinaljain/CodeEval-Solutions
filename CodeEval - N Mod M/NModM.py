'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    nums = map(int, test.strip().split(","))
    if nums[0] < nums[1]:
        print nums[0]
    print nums[0] - nums[1]*(nums[0]/nums[1])
test_cases.close()
