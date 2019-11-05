#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s.split(":")[0]=="12":
        if s.split(":")[2][-2:]=="AM":
            return "00"+s[2:-2]
        else:
            return s[:8]
    else:
        if s.split(":")[2][-2:]=="AM":
            return s[:8]
        else:
            h = int(s.split(":")[0])+12
            if h >=24:
                h-=24
                h="0"+str(h)
            else:
                h=str(h)
    return h+s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
