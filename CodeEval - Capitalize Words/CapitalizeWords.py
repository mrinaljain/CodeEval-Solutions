'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    words = test.strip().split(' ')
    answer = []
    for word in words:
        lw = list(word)
        lw[0] = lw[0].upper()
        temp = "".join(lw)
        answer.append(temp)
    print ' '.join(answer)
test_cases.close()