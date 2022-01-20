from collections import deque
class Graph:
	def __init__(self,nodes,adj):
		self.nodes=nodes
		self.adj=adj

	def bfs(self):
		visited=[0]*self.nodes
		buffer=deque()
		bfs=[]
		for i in range(1,self.nodes+1):
			if visited[i-1]==0:
				buffer.appendleft(i)
				while len(buffer)!=0:
					node=buffer.pop()
					if visited[node-1]==0:
						buffer.extendleft(self.adj[node-1])
						bfs.append(node)
						visited[node-1]=1
		return " ".join(str(elem) for elem in bfs)


	def dfs(self):
		dfs=[]
		visited=[0]*self.nodes
		buffer=deque()
		for i in range(1,self.nodes+1):
			if visited[i-1]==0:
				buffer.appendleft(i)
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


	def cycleBfs(self):
		visited=[0]*self.nodes
		buffer=deque()
		bfs=[]
		cycle=False
		for i in range(1,self.nodes+1):
			if visited[i-1]==0:
				buffer.appendleft([i,-1])
				while len(buffer)!=0:
					node,origin=buffer.pop()
					visited[node-1]=1
					for nodes in self.adj[node-1]:
						if visited[nodes-1]==1:
							if nodes!=origin:
								cycle=True
						else:
							buffer.appendleft([nodes,node])
							visited[nodes-1]=1
		return cycle
n=11
m=[[1,2],[2,4],[3,5],[5,10],[5,6],[6,7],[7,8],[10,9],[9,8],[8,11]]
adj=[[] for _ in range(n)]
for edge in m:
	i,j=edge[0],edge[1]
	adj[i-1].append(j)
	adj[j-1].append(i)
print(adj)
g=Graph(n,adj)
print(g.bfs())
print(g.dfs())
print(g.cycleBfs())