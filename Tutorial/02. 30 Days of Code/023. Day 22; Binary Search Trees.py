# Problem: https://www.hackerrank.com/challenges/30-binary-search-trees/problem
# Difficulty : Easy
# Score : 30

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        left = 0
        right = 0
        if root.right != None:
            right += 1 + self.getHeight(root.right)
        if root.left != None:
            left += 1 + self.getHeight(root.left)
        return max(left, right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
