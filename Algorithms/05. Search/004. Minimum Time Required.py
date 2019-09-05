# Problem: https://www.hackerrank.com/challenges/minimum-time-required/problem
# Difficulty : Medium
# Score : 35


import math
import os

def minTime(machines, goal):
    minday = math.ceil(goal / len(machines)) * min(machines)
    maxday = math.ceil(goal / len(machines) * max(machines))

    while minday < maxday:
        day = (maxday + minday) // 2
        if sum(day // m for m in machines) >= goal:
            maxday = day
        else:
            minday = day + 1

    return minday

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])
    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans))
    fptr.close()
