# Problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# Difficulty : Easy
# Score : 15

import os

def catAndMouse(x, y, z):
    a = abs(x-z)
    b = abs(y-z)

    if a == b:
        return "Mouse C"
    elif a < b:
        return "Cat A"
    else:
        return "Cat B"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
