#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
i = 1
j = 0
numswaps = 0
while i < n:
    for items in range(0,len(a)-1):
        for j in range(0,len(a)-1):
            if a[j + 1] < a [j]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                j+=1
                numswaps +=1
        #print(a)
    i+=1
print("Array is sorted in",numswaps,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[len(a)-1])
