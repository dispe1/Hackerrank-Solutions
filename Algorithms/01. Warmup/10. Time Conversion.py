# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Difficulty : Easy
# Score : 15

import os

def timeConversion(s):
    a = int(s[:2])

    if "PM" in s:
        if a != 12:
            a += 12
        a = str(a)
    else:
        if a == 12:
            a = '00'
        else:
            a = '0' + str(a)

    s = s[:8]
    s = a + s[2:]

    return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result)
    f.close()
