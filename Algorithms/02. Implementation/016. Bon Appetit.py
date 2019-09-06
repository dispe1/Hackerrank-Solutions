# Problem: https://www.hackerrank.com/challenges/bon-appetit/problem
# Difficulty : Easy
# Score : 10

def bonAppetit(bill, k, b):
    s = sum(bill)
    s -= bill[k]

    sharedCost = s // 2

    if sharedCost == b:
        print('Bon Appetit')
    else:
        print(b- sharedCost)

if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())

    bonAppetit(bill, k, b)
