'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    word = list(test.strip())
    switch = []
    for x in word:
        if x.isupper(): switch.append(x.lower())
        elif x.islower(): switch.append(x.upper())
        else: switch.append(x)
    print "".join(switch)
test_cases.close()