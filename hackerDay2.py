import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    
    sub_total = meal_cost * (tax_percent * 1/100)
    with_tip = meal_cost * (tip_percent * 1/100)
    total_bill = round(sub_total + meal_cost + with_tip)
    print(total_bill)

def main():
    meal_cost = float(input())
    tip_percent = float(input())
    tax_percent = float(input())
    
    solve(meal_cost, tip_percent, tax_percent)
    
if __name__ == "__main__":
    main()

