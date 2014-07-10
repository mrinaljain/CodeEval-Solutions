'''
Created on Jul 2, 2014

@author: Bert
'''


import sys
import math

test_cases = open(sys.argv[1])

for test in test_cases:
    nums = map(int, list(test.strip()))
    exps = [len(nums)]*len(nums)
    print int(test)==sum(map(math.pow, nums, exps))

test_cases.close()