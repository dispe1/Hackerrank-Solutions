# Problem: https://www.hackerrank.com/challenges/30-linked-list/problem
# Difficulty : Easy
# Score : 30

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head == None:
            return Node(data)

        node = head

        while node.next != None:
            node = node.next

        node.next = Node(data)

        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head); 	  
