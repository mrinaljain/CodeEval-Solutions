'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
test_cases = open(sys.argv[1], 'r')

for line in test_cases:
    l = line.strip().split(' ')
    idx = l.pop()
    l = l[::-1]
    try: print l[int(idx)-1]
    except: pass
    
test_cases.close()
