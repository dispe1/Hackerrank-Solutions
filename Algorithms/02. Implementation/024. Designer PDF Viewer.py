# Problem: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# Difficulty : Easy
# Score : 20

import os

def designerPdfViewer(h, word):
    arr = [h[ord(w)-97] for w in word]
    answer = len(arr) * max(arr)

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))
    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result))
    fptr.close()
