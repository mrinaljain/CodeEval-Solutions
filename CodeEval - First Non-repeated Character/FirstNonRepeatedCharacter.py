'''
Created on Jul 2, 2014

@author: Bert
'''

import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().lower()
    counts = {'a':0,
              'b':0,
              'c':0,
              'd':0,
              'e':0,
              'f':0,
              'g':0,
              'h':0,
              'i':0,
              'j':0,
              'k':0,
              'l':0,
              'm':0,
              'n':0,
              'o':0,
              'p':0,
              'q':0,
              'r':0,
              's':0,
              't':0,
              'u':0,
              'v':0,
              'w':0,
              'x':0,
              'y':0,
              'z':0}
    
    sent = list(line)
    for l in sent:
        try: counts[l] += 1
        except: pass

    singles = [k for k, v in counts.iteritems() if v == 1]

    for l in sent:
        if l in singles:
            print l
            break
    
test_cases.close()