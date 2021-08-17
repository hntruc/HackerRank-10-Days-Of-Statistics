#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
def quartiles(arr):
    arr = sorted(arr)
    # Write your code here
    if (len(arr) % 2 == 0):
        Q2 = (arr[len(arr)//2] + arr[len(arr)//2 -1])/2
    else:
        Q2 = arr[len(arr)//2]    
    return Q2

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    return round(float(values - freqs),1)

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))
    
    data = [val[i] for i in range(n) for j in range(freq[i])]
    
    data = sorted(data)

    size = len(data)

    Q1 = quartiles(data[:(size//2)])

    if (size) % 2 == 0:
        Q3 = quartiles(data[size//2:])
    else:
        Q3 = quartiles(data[size//2+1:])


    print(interQuartile(Q3, Q1))
