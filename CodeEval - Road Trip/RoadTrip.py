'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().rstrip(';').split('; ')
    dist = []
    for s in line:
        pair = s.split(',')
        dist.append(int(pair[1]))
    
    dist = sorted(dist)
#     print dist
    ans = []
    ans.append(dist[0])
    for i in xrange(len(dist)):
        try: ans.append(dist[i+1]-dist[i])
        except: pass
#     print ans
    print ','.join(str(x) for x in ans)
test_cases.close()