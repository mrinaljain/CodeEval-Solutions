'''
Created on Jul 2, 2014

@author: Bert
'''
import sys
 
test_cases = open(sys.argv[1], 'r')
 
for test in test_cases:
    if test.rstrip() == "":
        continue
    test = test.rstrip()

    strang = test.split(" ")

    
    for word in reversed(range(0, len(strang))):
        print strang[word],
    print ""
test_cases.close()