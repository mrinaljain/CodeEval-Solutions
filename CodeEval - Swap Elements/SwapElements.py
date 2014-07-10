'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(' : ')
    first = line[0].strip().split(' ')
    second = line[1].strip().split(', ')
    for combo in second:
        idx = map(int, combo.split('-'))
        temp = first[idx[0]]
        first[idx[0]] = first[idx[1]]
        first[idx[1]] = temp
    for x in first: print x,
    print
test_cases.close()