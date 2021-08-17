#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr)//len(arr)
    result = 0
    for a in arr:
        result += pow((a-mean),2)
    return round(math.sqrt(result/len(arr)),1)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    print(stdDev(vals))
