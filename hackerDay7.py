#!/bin/python3

import math
import os
import random
import re
import sys

def main():
    rev_arr(arr)

def rev_arr(arr):
    rev = str(arr[::-1]).strip('[]').replace(',','')
    #cannot use strip on lists
    print(rev)   
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))   
    main()
