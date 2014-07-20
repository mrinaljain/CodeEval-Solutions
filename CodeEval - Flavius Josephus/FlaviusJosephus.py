'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(',')
    n = int(line[0])

    lst = [x for x in xrange(n)]
    ans = ''
    skip = int(line[1])
    
    skip -= 1
    idx = skip
    while len(lst) > 0:
        ans += str(lst.pop(idx))+' '
        try: idx = (idx + skip) % len(lst)
        except: pass
        
    print ans
    
test_cases.close()