'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    prep = test.strip().split('|')
    first = map(int, list(prep[0].strip().split(' ')))
    second = map(int, list(prep[1].strip().split(' ')))
    for x in range(0,len(first)):
        print first[x]*second[x],
    print
test_cases.close()