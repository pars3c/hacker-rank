#!/bin/python3

import math
import os
import random
import re
import sys
     
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, n):
    '''
    Reverse the list, in this case turn 0s to 1s and 1s to 0s

    '''
    for i in range(len(c)):
        
        if c[i] == 0:
            c[i] = 1
        elif c[i] == 1:
            c[i] = 0

    total_sum = 0
    for i in range(0, len(c)): # For each element in the list
        try:
            if (c[i] == 1 and c[i+1] == 1 and c[i+2] == 1): # If there are three 1s in a row i.e ([1,1,1]) turn the middle one into 0
                c[i+1] = 0
        except:
            pass
        if c[i] == 1 and i != 0: # The starting point ( the first step ) does not count as a step
            total_sum += 1

    return total_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, n)

    fptr.write(str(result) + '\n')

    fptr.close()
