#hackerrank.com Counting Valley Challenge 
#updated from forked file in Dec. 28, 2019

import os
import sys
import time

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0
    valleyCount = 0
    valley = False

    for step in s:
        if step == "D":
            altitude-=1
            if altitude < 0 and valley == False:
                valley = True
                valleyCount+=1
        if step == "U":
            altitude+=1
            if altitude >= 0 and valley == True:
                valley = False

    return (valleyCount)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
