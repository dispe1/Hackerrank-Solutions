# Problem: https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
# Difficulty : Hard
# Score : 80


def matrixRotation(matrix, r):
    n, m = len(matrix), len(matrix[0])

    for k in range(min(n, m)//2):
        layer = []
        rotation = r % (2 * (n+m-2-4*k))

        #top
        for i in range(k, m-k):
            layer.append(matrix[k][i])
        #right
        for i in range(k+1, n-k-1):
            layer.append(matrix[i][m-k-1])
        #bottom
        for i in range(m-k-1, k-1, -1):
            layer.append(matrix[n-k-1][i])
        #left
        for i in range(n-k-2, k, -1):
            layer.append(matrix[i][k])

        l = 0
        #top
        for i in range(k, m-k):
            matrix[k][i] = layer[(l+rotation) % len(layer)]
            l += 1
        #right
        for i in range(k+1, n-k-1):
            matrix[i][m-k-1] = layer[(l+rotation) % len(layer)]
            l += 1
        #bottom
        for i in range(m-k-1, k-1, -1):
            matrix[n-k-1][i] = layer[(l+rotation) % len(layer)]
            l += 1
        #left
        for i in range(n-k-2, k, -1):
            matrix[i][k] = layer[(l+rotation) % len(layer)]
            l += 1

    for i in matrix:
        print(" ".join(map(str, i)))

if __name__ == '__main__':
    mnr = input().rstrip().split()
    m = int(mnr[0])
    n = int(mnr[1])
    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
