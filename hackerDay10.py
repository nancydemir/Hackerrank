#!/bin/python3

import math
import os
import random
import re
import sys

"""def to_binary(n):   
   if n > 1:
        #keep dividing by 2
        to_binary(n//2)   
   result = n%2
   print(result,end="")
   count_ones(result) 

def count_ones(result):
   if result == 1:
        print("in count_ones, result = ",result)
        consecutive = count +  1
        print(consecutive)
   else:       
        print("zero")
   print("consecutive ones:",consecutive)
   return"""
       
#def without_recursion(n):

#without_recursion(n):

def main():
    n = int(input())
    to_binary(n)
       
def to_binary(n):
    consecutive = 0
    count = 0
    #get remainders of 1 and 0
    mylist = []
    while n >= 1:
        n = n//2
        rem = n % 2
        if rem == 1:
            mylist.append(rem)
            count +=1 
            if count >= consecutive:
                consecutive = count
            else:
                count = 0
          
    #we want to count consecutive 1's in the binary number
    
    print(consecutive)
  
if __name__ == '__main__':
    main()
    
    
   
    
