# Problem: https://www.hackerrank.com/challenges/sparse-arrays/problem
# Difficulty : Medium
# Score : 25

import os

def matchingStrings(strings, queries):
    result = []

    for q in queries:
        result.append(strings.count(q))

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())
    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.close()
