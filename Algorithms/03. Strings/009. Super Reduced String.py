# Problem: https://www.hackerrank.com/challenges/reduced-string/problem
# Difficulty : Easy
# Score : 10

import os

def superReducedString(s):
    reducedString = []

    for i in s:
        if len(reducedString) == 0 or i != reducedString[-1]:
            reducedString.append(i)
        else:
            reducedString.pop()


    if len(reducedString) == 0:
        return "Empty String"

    return ''.join(reducedString)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result)
    fptr.close()
