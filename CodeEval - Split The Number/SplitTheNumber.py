'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(' ')
    num = list(line[0])
    let = list(line[1])
    if '+' in let:
        idx = let.index('+')
        print int(line[0][:idx])+int(line[0][idx:])
    elif '-' in let:
        idx = let.index('-')
        print int(line[0][:idx])-int(line[0][idx:])
    
test_cases.close()