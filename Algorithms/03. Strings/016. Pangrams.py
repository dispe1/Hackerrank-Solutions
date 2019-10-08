# Problem: https://www.hackerrank.com/challenges/pangrams/problem
# Difficulty : Easy
# Score : 20

import os
from collections import Counter

def pangrams(s):
    return 'pangram' if len(Counter(s.lower())) == 27 else 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result)
    fptr.close()
