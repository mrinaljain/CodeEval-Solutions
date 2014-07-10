'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(' ')
#     print line
    ans = 0
    for x in xrange(10):
#         print 'number of',x,':',line.count(str(x))
        if line.count(str(x))==1:
            ans = str(x)
            break
    try: print line.index(ans)+1
    except: print 0
test_cases.close()