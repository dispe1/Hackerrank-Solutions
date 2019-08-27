# Problem: https://www.hackerrank.com/challenges/2d-array/problem
# Difficulty : Easy
# Score : 15

import os

def hourglassSum(arr):
	max = -1000
	x = len(arr)
	y = len(arr[0])

	for i in range(x-2):
		for j in range(y-2):
			value = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
			if value > max:
				max = value
	return max

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	arr = []

	for _ in range(6):
		arr.append(list(map(int, input().rstrip().split())))

	result = hourglassSum(arr)

    fptr.write(str(result))
