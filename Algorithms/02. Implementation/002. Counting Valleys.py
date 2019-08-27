# Problem: https://www.hackerrank.com/challenges/counting-valleys/problem
# Difficulty : Easy
# Score : 15

import os

def countingValleys(n, s):
	level = 0
	count = 0

	for i in range(1,n+1,1):
		if s[i-1] == "U":
			level += 1
			if level == 0:
				count += 1
		else:
			level -=1

	return count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())
	s = input()

	result = countingValleys(n, s)

	fptr.write(str(result))
    fptr.close()
