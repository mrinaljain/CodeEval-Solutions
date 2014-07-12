'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
 
test_cases = open(sys.argv[1], 'r')

racemap = []
for test in test_cases:
    racemap.append(list(test.strip()))

lz = []
ans = racemap
pidx = racemap[0].index('_')

for i, row in enumerate(racemap):
    if 'C' in row: 
        if row.index('C') == pidx: 
            lz.append('|')
        elif row.index('C') > pidx: 
            lz.append('\\')
        elif row.index('C') < pidx: 
            lz.append('/')
        pidx = row.index('C')
    else: 
        if row.index('_') == pidx: 
            lz.append('|')
        elif row.index('_') > pidx: 
            lz.append('\\')
        elif row.index('_') < pidx: 
            lz.append('/')
        pidx = row.index('_')

for i, row in enumerate(ans):
    if 'C' in row:
        row[row.index('C')] = lz[i]
    else:
        row[row.index('_')] = lz[i]

for x in ans:
    print ''.join(e for e in x)
         
test_cases.close()
