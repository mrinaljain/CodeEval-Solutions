'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    seq = ''
    length = 0
    line = list(test.strip())
    for x in line:
        seq += x
        check = ''
        try: check = test.strip()[-len(seq):]
        except: pass
        if check == seq:
            print len(seq)
            break
test_cases.close()