# Problem: https://www.hackerrank.com/challenges/caesar-cipher-1/problem
# Difficulty : Easy
# Score : 15

import os

def shiftAlphabet(c, k):
    if 65 <= c <= 90:
        c += k
        if c < 65:
            c += 26
        elif c > 90:
            c -= 26
    elif 97 <= c <= 122:
        c += k
        if c < 97:
            c += 26
        elif c > 122:
            c -= 26

    return chr(c)

def caesarCipher(s, k):
    ret = []
    k %= 26
    for i in s:
        ret.append(shiftAlphabet(ord(i), k))

    return ''.join(ret)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()
    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result)
    fptr.close()
