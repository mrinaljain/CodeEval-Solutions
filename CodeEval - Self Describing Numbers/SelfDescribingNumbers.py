'''
Created on Jul 2, 2014

@author: Bert
'''

import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = list(test.strip())
    counts = {'0':0,
              '1':0,
              '2':0,
              '3':0,
              '4':0,
              '5':0,
              '6':0,
              '7':0,
              '8':0,
              '9':0}
    for num in line:
        counts[num] += 1
#     print counts
    ans = ''
    for i in xrange(len(line)):
        ans += str(counts[str(i)])
    if test.strip() == ans:
        print 1
    else: print 0

test_cases.close()