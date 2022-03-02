class PriorityQueue:
    def __init__(self):
        self.buffer=list()
    def push(self,dist,node):
        self.buffer.insert(0,[dist,node])
    def pop(self):
        min=0
        for i in range(1,len(self.buffer)):
            if self.buffer[i][0]<self.buffer[min][0]:
                min=i
        item=self.buffer[min]
        del self.buffer[min]
        return item
    def display(self):
        return self.buffer

n=4
m=[[1,2,5],[1,4,40],[2,3,10],[3,4,10]]
adj =[[] for _ in range(n)]
for edge in m:
    i,j,weight=map(int,edge)
    adj[i-1].append([j,weight])
print(adj)