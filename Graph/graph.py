from collections import deque
class Graph:
	def __init__(self,nodes,adj):
		self.nodes=nodes
		self.adj=adj

	def bfs(self):
		visited=[0]*self.nodes
		buffer=deque()
		bfs=[]
		for i in range(self.nodes):
			buffer.appendleft(i)
			while len(buffer)!=0:
				node=buffer.pop()
				if visited[node]==0:
					buffer.extendleft(self.adj[node])
					bfs.append(node)
					visited[node]=1
		return " ".join(str(elem) for elem in bfs)


	def dfs(self,func=None):
		dfs=[]
		visited=[0]*self.nodes
		buffer=deque()
		for i in range(self.nodes):
			buffer.appendleft(i)
			while len(buffer)!=0:
				curr=buffer.pop()
				if visited[curr]==0:
					if func=="Toposort":
						self.sorting(curr,visited,self.adj,dfs,buffer)
					else:
						self.traversal(curr,visited,self.adj,dfs,buffer)
		return " ".join(str(elem) for elem in dfs)

	def traversal(self,node,visited,adj,dfs,buffer):
		dfs.append(node)
		visited[node]=1
		for nodes in adj[node]:
			buffer.appendleft(nodes)
			if visited[nodes]==0:
				self.traversal(nodes,visited,self.adj,dfs,buffer)

	def toposortBfs(self):
		toposort=[]
		indegree=[0 for _ in range(self.nodes)]
		for node in self.adj:
			for elem in node:
				indegree[elem]+=1
		buffer=deque()
		self.indegreeCalc(buffer,indegree)
		while len(buffer)!=0:
			curr=buffer.pop()
			toposort.append(curr)
			for nodes in adj[curr]:
				indegree[nodes]-=1
			self.indegreeCalc(buffer,indegree)
		return " ".join(str(elem) for elem in toposort)
	
	def indegreeCalc(self,buffer,indegree):
		for i in range(self.nodes):
			if indegree[i]==0:
				buffer.appendleft(i)
				indegree[i]-=1
	
	def toposortDfs(self):
		return self.dfs("Toposort")
	
	def sorting(self,node,visited,adj,dfs,buffer):
		visited[node]=1
		for nodes in adj[node]:
			buffer.appendleft(nodes)
			if visited[nodes]==0:
				self.traversal(nodes,visited,self.adj,dfs,buffer)
		dfs.append(node)
		
	def cycleBfs(self):
		visited=[0]*self.nodes
		buffer=deque()
		bfs=[]
		cycle=False
		for i in range(self.nodes):
			if visited[i]==0:
				buffer.appendleft([i,-1])
				while len(buffer)!=0:
					node,origin=buffer.pop()
					visited[node]=1
					for nodes in self.adj[node]:
						if visited[nodes]==1:
							if nodes!=origin:
								cycle=True
						else:
							buffer.appendleft([nodes,node])
							visited[nodes]=1
		return cycle
n=6
m=[[2,3],[3,1],[4,0],[4,1],[5,0],[5,2]]
adj=[[] for _ in range(n)]
for edge in m:
	i,j=edge[0],edge[1]
	adj[i].append(j)
g=Graph(n,adj)
# print(g.bfs())
print(g.toposortBfs())
# print(g.dfs())
# print(g.toposortDfs())
print(g.cycleBfs())