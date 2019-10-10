# Problem: https://www.hackerrank.com/challenges/funny-string/problem
# Difficulty : Easy
# Score : 25

import os

def funnyString(s):
    r = s[::-1]

    s = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)]
    r = [abs(ord(r[i]) - ord(r[i+1])) for i in range(len(r)-1)]

    if s == r:
        return "Funny"

    return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
