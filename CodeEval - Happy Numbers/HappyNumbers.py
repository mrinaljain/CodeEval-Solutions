'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    num = map(int, list(test.strip()))
#     print num
    temp = []
    count = 0
    while len(num) != 1 and num[0] != 1 and count < 1000000000000000:
        t = 0
        for n in num:
            t += n*n
#             print t,
        num = map(int, list(str(t)))
        count += 1
#         print int(''.join(str(e) for e in num))
        
    if int(''.join(str(e) for e in num))==1:
        print 1
    else: print 0
test_cases.close()
