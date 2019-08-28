# Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
# Difficulty : Medium
# Score : 50

import os
import collections

def sherlockAndAnagrams(s):
    pair = []
    count = collections.Counter()
    result = 0

    for i in range(1,len(s)):
        for j in range(0,len(s)-i +1):
            c = collections.Counter()
            for k in range(j,j+i):
                if s[k] in c:
                    c[s[k]] +=1
                else:
                    c[s[k]] = 1
            pair.append(tuple(sorted(c.items())))

    for i in pair:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in count:
        result += (int) ((count[i] * (count[i]-1)) / 2 ) # nC2 = (n*(n-1)) / 2

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
