# Problem: https://www.hackerrank.com/challenges/strong-password/problem
# Difficulty : Easy
# Score : 15

import os

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    requiredNumber = 1
    requiredLower = 1
    requiredUpper = 1
    requiredSpecial = 1

    for i in password:
        if i in numbers:
            requiredNumber = 0
        elif i in lower_case:
            requiredLower = 0
        elif i in upper_case:
            requiredUpper = 0
        elif i in special_characters:
            requiredSpecial = 0

    ret = requiredNumber + requiredLower + requiredUpper + requiredSpecial

    if len(password) + ret < 6:
        return 6 - len(password)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer))
    fptr.close()
