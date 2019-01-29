#!/bin/python3

import math
import os
import random
import re
import sys


def weird(N):
    if 1 <= N <= 100:  
            
        if (N % 2 == 0) and (2 <= N <= 5 or N > 20):
            print("Not Weird")
        elif N % 2 == 0 and 6 <= N <= 20:
            print("Weird")  
        else: 
            print("Weird")
            
def main():
    N = int(input())
    weird(N)

if __name__ == '__main__':
    main()
