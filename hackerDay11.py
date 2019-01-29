#!/bin/python3


import math
import os
import random
import re
import sys
from array import *

def main():
    arr = [[1, 1, 1 ,0 ,0 ,0], [0, 1 ,0 ,0 ,0 ,0],[ 1 ,1 ,1 ,0 ,0 ,0],[0 ,0 ,2 ,4 ,4 ,0],[0 ,0 ,0 ,2 ,0 ,0],[0 ,0 ,1 ,2 ,4 ,0]]
    getSums(arr)
''' for m in arr:
    for n in m:
        print(n,end = " ")
    print()'''

def getSums(arr):
    i= 0
    j = 0
    maxSum = -64
    tempSum = 0
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            tempSum = arr[i][j]+ arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1] + arr[i+2][j]+ arr[i+2][j+1]+ arr[i+2][j+2]
            #print("tempSum=",tempSum)
            #print("maxSum=",maxSum)
            if tempSum > maxSum:
                maxSum = tempSum
            j+=1
        i+=1 
    print(maxSum)

if __name__ == '__main__':       
        main()
