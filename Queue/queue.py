from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()

    def is_empty(self):
        return len(self.buffer)==0
    
    def enqueue(self,data):
        self.buffer.appendleft(data)

    def deque(self):
        self.deque.pop()
    
    def size(self):
        return len(self.buffer)
