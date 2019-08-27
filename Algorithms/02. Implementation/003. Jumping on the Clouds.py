# Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# Difficulty : Easy
# Score : 20

import os

def jumpingOnClouds(c):
	r = 0
	p = 0

	while p < len(c)-1:
		if p+2 < len(c) and c[p+2] == 0:
			p += 2
		else:
			p += 1
		r += 1

	return r

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())
	c = list(map(int, input().rstrip().split()))

	result = jumpingOnClouds©

	fptr.write(str(result))
    fptr.close()
