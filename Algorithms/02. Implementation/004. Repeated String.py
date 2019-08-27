# Problem: https://www.hackerrank.com/challenges/repeated-string/problem
# Difficulty : Easy
# Score : 20

import os

def repeatedString(s, n):
c = s.count('a')
l = len(s)
p = n // l
r = n % l

c *= p
r = s[:r].count('a')

return c + r

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()
	n = int(input())

	result = repeatedString(s, n)

	fptr.write(str(result))
    fptr.close()
