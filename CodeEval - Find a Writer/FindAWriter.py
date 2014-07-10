'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    if test.strip() == '': continue
    both = test.strip().split('|')
    first = list(both[0])
    second = map(int, list(both[1].strip().split(' ')))
    answer = ''
    for num in second: answer+=first[num-1]
    print answer
test_cases.close()