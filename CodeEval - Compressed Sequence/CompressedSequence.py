'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(' ')
    line.append('')
    ans = []
    prev = ''
    count = 0
    for num in line:
        if num != prev:
            if count>0: ans.append(count)
            if prev != '': ans.append(prev)
            prev = num
            count = 1
        elif num == prev:
            count += 1
    print ' '.join(str(x) for x in ans)
test_cases.close()