# Problem: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
# Difficulty : Easy
# Score : 20

import os

def rotLeft(a, d):
	return a[d:] + a[:d]

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nd = input().split()
	n = int(nd[0])
	d = int(nd[1])
	a = list(map(int, input().rstrip().split()))

	result = rotLeft(a, d)

	fptr.write(' '.join(map(str, result)))
    fptr.close()
