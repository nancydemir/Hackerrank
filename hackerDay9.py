import re
import sys

# Complete the factorial function below.
def factorial(n):


    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
   
       

    

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)
    print(result)