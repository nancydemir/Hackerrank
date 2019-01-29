import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.

def aVeryBigSum(ar):
    
    summed = 0    
    for n in ar:        
        summed +=n       
    print(summed)
    
if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
