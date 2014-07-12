'''
Created on Jul 2, 2014

@author: Bert
'''

for i in range(1,13):
    for j in range(1,13):
        if j < 12: print str(i*j).rjust(4),
        else: print str(i*j).rjust(4).rstrip()