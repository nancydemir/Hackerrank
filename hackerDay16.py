#!/bin/python3

import sys

S = input().strip()
try:
    value = int(S)
    print(value)
except ValueError:
    print("Bad String")
 
        
        
