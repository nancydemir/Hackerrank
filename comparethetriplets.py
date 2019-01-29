#!/bin/python3

import math
import os
import random
import re
import sys      
# Complete the compareTriplets function below. 
    
def compareTriplets(alist, blist):
    i = 0
    atakes_it = 0
    btakes_it = 0
    returnarray = []
    while i < 3:
        if alist[i] > blist[i]:
            atakes_it+=1
        else:
            if blist[i] > alist[i]:
                btakes_it+=1
        i+=1
    returnarray = [atakes_it,btakes_it]
    return(returnarray)

def main(): 
#fptr = open(os.environ['OUTPUT_PATH'], 'w')
#fptr.write(' '.join(map(str, result)))
#fptr.write('\n')
#fptr.close()
    alist = list(map(int, input().rstrip().split()))
    blist = list(map(int, input().rstrip().split()))
    result = compareTriplets(alist, blist)
    print(result)
    
if __name__ == '__main__':
    main()

