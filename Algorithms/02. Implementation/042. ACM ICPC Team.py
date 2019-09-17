# Problem: https://www.hackerrank.com/challenges/acm-icpc-team/problem
# Difficulty : Easy
# Score : 25

import os

def acmTeam(topic):
    maxValue = 0
    maxCount = 0

    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            tmp = 0
            for k in range(len(topic[i])):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    tmp += 1

            if tmp == maxValue:
                maxCount += 1
            elif tmp > maxValue:
                maxValue = tmp
                maxCount = 1

    return [maxValue, maxCount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.close()
