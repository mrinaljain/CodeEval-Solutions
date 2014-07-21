'''
Created on Jul 2, 2014

@author: Bert
'''

import sys

def rowCheck(array, size):
    for row in array:
        check = [x for x in xrange(1,size+1)]
        for col in row:
            try: check.remove(col)
            except: pass
        if len(check) != 0: return False
    return True

def colCheck(array, size):
    array2 = zip(*array)
    for row in array2:
        check = [x for x in xrange(1,size+1)]
        for col in row:
            try: check.remove(col)
            except: pass
        if len(check) != 0: return False
    return True

def squareCheck4(array, size):
    lzt = []
    arrays = []
    
    a = zip(*array)[::-1]
    b = zip(*a)[::-1]
    c = zip(*b)[::-1]
    d = zip(*c)[::-1]
    
    arrays.append(a)
    arrays.append(b)
    arrays.append(c)
    arrays.append(d)
    
    for k in arrays:
        square = []
        square.append(k[0][0])
        square.append(k[0][1])
        square.append(k[1][0])
        square.append(k[1][1])
        lzt.append(square)
    
    for row in lzt:
        check = [x for x in xrange(1,size+1)]
        for col in row:
            try: check.remove(col)
            except: pass
        if len(check) != 0: return False
    return True

def squareCheck9(array, size):
    lzt = []
    arrays = []
    
    a = zip(*array)[::-1]
    b = zip(*a)[::-1]
    c = zip(*b)[::-1]
    d = zip(*c)[::-1]
    
    arrays.append(a)
    arrays.append(b)
    arrays.append(c)
    arrays.append(d)
    
    for k in arrays:
        square = []
        square.append(k[0][0])
        square.append(k[0][1])
        square.append(k[1][0])
        square.append(k[1][1])
        square.append(k[0][2])
        square.append(k[1][2])
        square.append(k[2][0])
        square.append(k[2][1])
        square.append(k[2][2])
        lzt.append(square)
    
    for row in lzt:
        check = [x for x in xrange(1,size+1)]
        for col in row:
            try: check.remove(col)
            except: pass
        if len(check) != 0: return False
    return True


test_cases = open(sys.argv[1])

for test in test_cases:
    line = test.strip().split(';')
    nums = map(int, line[1].split(','))
    size = int(line[0])
    grid = [[0 for x in xrange(size)] for x in xrange(size)] 
    check = [x for x in xrange(1,size+1)]

    n = 0
    col = 0
    for i in xrange(len(nums)):
        grid[n][col] = nums[i]
        col += 1
        if col == size:
            n += 1
            col = 0  
            
    if size == 4: print colCheck(grid, size) and rowCheck(grid, size) and squareCheck4(grid, size)
    elif size == 9: print colCheck(grid, size) and rowCheck(grid, size) and squareCheck9(grid, size)
    else: print 'ERROR: Size is not 4 or 9'
    
test_cases.close()