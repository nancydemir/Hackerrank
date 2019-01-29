import math
import os
import random
import re
import sys

def multiples(n):
    i = 1
    while i <= 10:
        print(n,"x",i,"=",n * i)
        i += 1

def main():
    n = int(input())
    multiples(n)
if __name__ == '__main__':
    main()
