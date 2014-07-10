'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    a = test.strip().split(";")
    set1 = set(a[0].split(","))
    set2 = set(a[1].split(","))
    z = sorted(set1 & set2)
    print ",".join(str(e) for e in z).rstrip()
test_cases.close()
