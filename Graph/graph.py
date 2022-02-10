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
n=6
m=[[2,3],[3,1],[4,0],[4,1],[5,0],[5,2]]
adj=[[] for _ in range(n)]
for edge in m:
	i,j=edge[0],edge[1]
	adj[i].append(j)
g=Graph(n,adj)
# print(g.bfs())
print(g.dfs())
print(g.toposortDfs())
# print(g.cycleBfs())