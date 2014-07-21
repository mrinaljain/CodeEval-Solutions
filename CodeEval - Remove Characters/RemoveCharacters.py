'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(',')
    remove = list(line[1])
    sent = line[0]

    for l in remove:
        if l != ' ':
            sent = sent.replace(l,'')
    print sent
    
    
test_cases.close()