from collections import deque

class Stack(object):
    def __init__(self):
        self.container=deque()
    def push(self,data):
        self.container.append(data)
    def pop(self):
        return self.container.pop()
    def peep(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def isEmpty(self):
        return len(self.container)==0

postfix="abc*d/+xyz*-+"
s=Stack()
for char in postfix:
    if char.isalpha():
        s.push(input("Enter the value of "+char+" " ))
    else:
        a=s.pop()
        b=s.pop()
        ans=eval(str(b)+char+str(a))
        s.push(int(ans))
print(s.pop())