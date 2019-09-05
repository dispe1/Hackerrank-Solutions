# Problem: https://www.hackerrank.com/challenges/grading/problem
# Difficulty : Easy
# Score : 10

import os

def gradingStudents(grades):
    result = []
    for grade in grades:
        q = grade // 5

        if grade < 38:
            result.append(grade)
        elif (q+1) * 5 - grade < 3:
            result.append( (q+1) * 5 )
        else:
            result.append( grade )

    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.close()
