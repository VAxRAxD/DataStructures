from collections import deque
class Graph:
	def __init__(self,nodes,start,adj):
		self.nodes=nodes
		self.start=start
		self.adj=adj

	def bfs(self):
		visited=[0]*self.nodes
		buffer=deque()
		buffer.appendleft(self.start)
		bfs=[]
		while len(buffer)!=0:
			node=buffer.pop()
			if visited[node-1]==0:
				buffer.extendleft(self.adj[node-1])
				bfs.append(node)
				visited[node-1]=1
			else:
				continue
		return " ".join(str(elem) for elem in bfs)

	def dfs(self):
		dfs=[]
		visited=[0]*self.nodes
		buffer=deque()
		buffer.appendleft(self.start)
		while len(buffer)!=0:
			curr=buffer.pop()
			if visited[curr-1]==0:
				self.traversal(curr-1,visited,self.adj,dfs,buffer)
		return " ".join(str(elem) for elem in dfs)

	def traversal(self,node,visited,adj,dfs,buffer):
		dfs.append(node+1)
		visited[node]=1
		for nodes in adj[node]:
			buffer.appendleft(nodes)
			if visited[nodes-1]==0:
				self.traversal(nodes-1,visited,self.adj,dfs,buffer)
n=5
m=[[1,2],[2,3],[2,4],[3,5],[4,5]]
start=5
adj=[[] for _ in range(n)]
for edge in m:
	i,j=edge[0],edge[1]
	adj[i-1].append(j)
	adj[j-1].append(i)
g=Graph(n,start,adj)
print(g.bfs())
print(g.dfs())