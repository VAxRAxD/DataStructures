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

infix="a+b/c*d-e"
postfix=""
precedence = {'+':1, '-':1, '*':2, '/':2, '^':3,'(':0}
operators=['+','-','/','*','%']
s=Stack()
for char in infix:
    if char=="(": s.push(char)
    elif char==")":
        while s.size()>0:
            elem=s.pop()
            if elem=="(":
                break
            else:
                postfix+=elem
    elif char.isalpha(): postfix+=char
    else:
        if s.isEmpty():
            s.push(char)
        else:
            if precedence[char]>precedence[s.peep()]:
                s.push(char)
            else:
                while (s.size()>0) and (precedence[char]<=precedence[s.peep()]):
                    postfix+=s.pop()
                s.push(char)
if s.size()>0:
    while s.size()>0:
        postfix+=s.pop()
print(postfix)