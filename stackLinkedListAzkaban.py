# Monk and Prisoner of Azkaban

# Monk's wizard friend Harry Potter is 
# # excited to see his Dad fight Dementors 
# and rescue him and his Godfather Sirius 
# Black. Meanwhile their friend Hermoine 
# is stuck on some silly arrays problem. 
# Harry does not have time for all this, 
# so he asked Monk to solve that problem 
# for Hermoine, so that they can go.

# The problem is given an array A
# having N integers, for each i (1<i<N)
# find x + y, where x is the largest number
# less than i such that A[x] > A[i] and y
# is the smallest number greater than i
# such that A[y] > A[i]. If there is
# no x < i such that A[x] > A[i] then
# take x = -1. Similarly, if there is no
# y > i such that A[y] > A[i], then take
# y = -1

# https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/monk-and-prisoner-of-azkaban/

class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def peek(self):
        return self.head
    
    def pop(self):
        if self.count == 0:
            return None
        else:
            temp = self.head
            self.removeFirst()
            return temp
            
    def removeFirst(self):
        temp = self.head
        self.head = None
        if temp != None:
            self.head = temp.next
        self.count -= 1

    def addFirst(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
        self.count += 1
        
    def printAll(self):
        if self.count == 0:
            print("No elements in stack")
            return
        if self.count == 1:
            print(self.head.value)
        else:
            currentNode = self.head
            while currentNode.next != None:
                print(currentNode.value)
                currentNode = currentNode.next
            print(currentNode.value)
        
a[n]
biggestNumber = Stack()
smallestNumber = Stack()
for index in a:
    for possibleBigNumber in range(a.length - index):
    for possibleSmallNumber in a:
