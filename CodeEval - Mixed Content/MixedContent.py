'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(',')
#     print line
    strangs = []
    nums = []
    for word in line:
        try: word = int(word)
        except: pass
        if isinstance(word, int):
            nums.append(word)
        else: strangs.append(word)
    
    if len(strangs)>0 and len(nums)>0:
        a = ','.join(str(x) for x in strangs)
        b = ','.join(str(x) for x in nums)
        print a+'|'+b
    elif not strangs: print ','.join(str(x) for x in nums)
    elif not nums: print ','.join(str(x) for x in strangs)
    else: print 'ERROR!'
test_cases.close()