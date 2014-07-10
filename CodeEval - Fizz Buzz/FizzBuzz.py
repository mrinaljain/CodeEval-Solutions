'''
Created on Jul 2, 2014

@author: Bert
'''

import sys
 
test_cases = open(sys.argv[1], 'r')
 
for test in test_cases:
    strang = test.split(" ")
    for num in range(1, int(strang[2])+1):
        if (num % int(strang[0]) == 0 and num % int(strang[1]) == 0):
            print "FB",
        elif num % int(strang[0]) == 0:
            print "F",
        elif num % int(strang[1]) == 0:
            print "B",
        else:
            print num,
    print ""
test_cases.close()
