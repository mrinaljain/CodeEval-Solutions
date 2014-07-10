'''
Created on Jul 2, 2014

@author: Bert
'''


import sys, re
from math import sqrt

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip()
    p = re.findall('(-?\d+\, -?\d+)', line)
    first = map(int, p[0].split(', '))
    second = map(int, p[1].split(', '))
    print '%0.f' % sqrt((first[0]-second[0])*(first[0]-second[0])+(first[1]-second[1])*(first[1]-second[1]))
test_cases.close()