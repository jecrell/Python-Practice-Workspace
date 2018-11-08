class Queue:
    def __init__(self):
        self.contents = []
        self.size = 0
    
    def Enqueue(self, data):
        self.contents.append(data)
        self.size += 1
