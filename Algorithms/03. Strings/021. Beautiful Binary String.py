# Problem: https://www.hackerrank.com/challenges/beautiful-binary-string/problem
# Difficulty : Easy
# Score : 20

import os

def beautifulBinaryString(b):
    ret = 0
    i = 0

    while i < len(b):
        if b[i:i+3] == "010":
            ret += 1
            i += 3
        else:
            i += 1

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result))
    fptr.close()
