'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = list(test.strip())
    trans = {'a':0,
             'b':1,
             'c':2,
             'd':3,
             'e':4,
             'f':5,
             'g':6,
             'h':7,
             'i':8,
             'j':9}
#     print line
    ans = ''
    for c in line:
        try: ans += str(int(c))
        except: pass
        if c in trans:
            ans += str(trans[c])
    if len(ans) > 0: print ans
    else: print 'NONE'

test_cases.close()