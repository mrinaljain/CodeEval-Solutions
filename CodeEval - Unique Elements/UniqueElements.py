'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if test == "": continue
    st = set(map(int, test.rstrip().split(",")))
    ans = ''
    for num in st: ans+=str(num)+','
    print ans.strip(',')
test_cases.close()
