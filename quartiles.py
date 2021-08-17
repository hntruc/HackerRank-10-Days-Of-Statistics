#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    arr = sorted(arr)
    # Write your code here
    if (len(arr) % 2 == 0):
        Q2 = (arr[len(arr)//2] + arr[len(arr)//2 -1])/2
    else:
        Q2 = arr[len(arr)//2]    
    return Q2
    
n = int(input().strip())

data = list(map(int, input().rstrip().split()))

data = sorted(data)

size = len(data)

Q2 = int(quartiles(data))

Q1 = int(quartiles(data[:(size//2)]))

if (size) % 2 == 0:
    Q3 = int(quartiles(data[size//2:]))
else:
    Q3 = int(quartiles(data[size//2+1:]))
        
print(Q1)
print(Q2)
print(Q3)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
