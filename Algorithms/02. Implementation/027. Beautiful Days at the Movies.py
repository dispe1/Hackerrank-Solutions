# Problem: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Difficulty : Easy
# Score : 15


import os

def beautifulDays(i, j, k):
    answer = 0

    for day in range(i,j+1):
        r = int(str(day)[::-1])

        if abs(day-r) % k == 0:
            answer += 1

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result))
    fptr.close()
