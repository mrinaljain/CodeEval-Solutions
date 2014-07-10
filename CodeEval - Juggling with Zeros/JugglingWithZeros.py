'''
Created on Jul 2, 2014

@author: Bert
'''


import sys

test_cases = open(sys.argv[1])

for test in test_cases:
    nums = test.strip().split(" ")
    strang = ""
    for num in range(0, len(nums)):        
        if num%2==0:
            if nums[num]=="0":
                strang += nums[num+1]
            elif nums[num]=="00":
                strang += nums[num+1].replace("0","1")
            else: print "ERROR!"
#     print "This is the binary string:",strang
#     print "This is the integer:",int(strang,2)
    print int(strang,2)
test_cases.close()