# Problem: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
# Difficulty : Easy
# Score : 5

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def insertNodeAtHead(llist, data):
    if llist == None:
        return SinglyLinkedListNode(data)
    else:
        l = SinglyLinkedListNode(data)
        l.next = llist
        return l

if __name__ == '__main__':
