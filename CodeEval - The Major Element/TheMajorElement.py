'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = map(int, test.strip().split(','))
    thresh = len(line)/2
#     print line, thresh
    mode = -1
    occurances = 0
    for x in range(max(line)):
#         print 'Line count',x,':',line.count(x)
        if line.count(x)>occurances:
            mode = x
            occurances = line.count(x)
    if occurances>thresh: print mode
    else: print 'None'
test_cases.close()