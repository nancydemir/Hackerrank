#!/bin/python3

import math
import os
import random
import re
import sys

#n=number of socks
#ar=the color of each sock

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    print(n,ar)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
        
n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

fptr.write(str(result) + '\n')

fptr.close()
