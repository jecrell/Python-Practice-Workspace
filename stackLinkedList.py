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
        
tempStack = Stack()
tempStack.addFirst(Node(10))
tempStack.addFirst(Node(33))
tempStack.addFirst(Node(12))
tempStack.addFirst(Node(2))
print("Peek ", tempStack.peek().value)
tempStack.addFirst(Node(81))
print("Pop ", tempStack.pop().value)
tempStack.printAll()