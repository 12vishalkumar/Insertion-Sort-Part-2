import math
import os
import random
import re
import sys
# Complete the 'insertionSort2' function below.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        j = i
        while(j>0 and arr[j] < arr[j-1]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
        st = str(arr)[1:-1].replace(',', '')
        print(st)            
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)