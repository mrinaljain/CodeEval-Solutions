'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = int(test.strip())
    if line < 0 or line > 100: print 'This program is for humans'
    elif line <= 2: print 'Home'
    elif line <= 4: print 'Preschool'
    elif line <= 11: print 'Elementary school'
    elif line <= 14: print 'Middle school'
    elif line <= 18: print 'High school'
    elif line <= 22: print 'College'
    elif line <= 65: print 'Work'
    elif line <= 100: print 'Retirement'

test_cases.close()