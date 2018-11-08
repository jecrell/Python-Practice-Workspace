# Monk and Prisoner of Azkaban

# Monk's wizard friend Harry Potter is 
# excited to see his Dad fight Dementors 
# and rescue him and his Godfather Sirius 
# Black. Meanwhile their friend Hermoine 
# is stuck on some silly arrays problem. 
# Harry does not have time for all this, 
# so he asked Monk to solve that problem 
# for Hermoine, so that they can go.

# Node and Stack classes

class Node:
    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.value = value

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
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
            self.head.prev = None
        else:
            self.tail = None
        self.count -= 1

    def addFirst(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = Node(value)
        else:
            temp = self.head
            self.head = Node(value)
            temp.prev = self.head
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

index = 0
stackA = Stack()
stackA.addFirst(5)
stackA.addFirst(4)
stackA.addFirst(1)
stackA.addFirst(3)
stackA.addFirst(2)
currentIndex = 1
currentNode = stackA.head
while currentNode != None:
    originVal = currentNode.value
    xVal = currentNode.value
    yVal = currentNode.value
    if currentIndex != 1:
        xNode = currentNode.prev
        while xNode != None:
            if xVal < xNode.value:
                xVal = xNode.value
            xNode = xNode.prev
    if currentIndex == stackA.count:
        yVal = -1
    else:
        yNode = currentNode.next
        while yNode != None:
            if yVal < yNode.value:
                yVal = yNode.value
            yNode = yNode.next
    if xVal == originVal:
        xVal = -1
    if yVal == originVal:
        yVal = -1
    print(xVal + yVal)
    currentNode = currentNode.next
    currentIndex += 1
            

