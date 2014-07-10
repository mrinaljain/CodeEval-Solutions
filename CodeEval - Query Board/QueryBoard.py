'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

qb = [[0 for x in xrange(256)] for x in xrange(256)]

for test in test_cases:
    line = test.strip().split(' ')
#     print line
    if line[0]=='SetRow':
        for x in xrange(256):
            qb[int(line[1])][x] = int(line[2])
    elif line[0]=='SetCol':
        for x in xrange(256):
            qb[x][int(line[1])] = int(line[2])
    elif line[0]=='QueryRow':
        ans = 0
        for x in xrange(256):
            ans += qb[int(line[1])][x]
        print ans
    elif line[0]=='QueryCol':
        ans = 0
        for x in xrange(256):
            ans += qb[x][int(line[1])]
        print ans
    else: print 'ERROR!'
test_cases.close()