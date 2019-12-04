# Problem: https://www.hackerrank.com/challenges/30-regex-patterns/problem
# Difficulty : Easy
# Score : 30

if __name__ == '__main__':
    N = int(input())
    ar = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if '@gmail.com' in emailID:
            ar.append(firstName)

    ar.sort()

    for i in ar:
        print(i)
