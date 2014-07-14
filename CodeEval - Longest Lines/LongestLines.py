


'''
Created on Jul 2, 2014

@author: Bert
'''

import sys, collections
test_cases = open(sys.argv[1], 'r')

infile = []
lengths = []

for line in test_cases:
    infile.append(line.strip())

topN = int(infile[0])
for i, l in enumerate(infile):
    if i > 0: 
        lengths.append(len(l))

infile.pop(0)
d = dict(zip(lengths, infile))
od = collections.OrderedDict(reversed(sorted(d.items())))
for i in range(topN): print od.popitem(0)[1]

test_cases.close()
