'''
Created on Jul 2, 2014

@author: Bert
'''


import sys, re

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(',')
    pat = line[1]+'$'
    p = re.compile(pat)
    test = p.findall(line[0])
    print len(test)
   
test_cases.close()