"""
ALGORITHM_DIJKSTRA
#n is total number of nodes
#d[1:n] is distance array where d[i] contains shortest distance from source to iᵗʰ vertex
#π[1:n] is source array where π[i]  contains the parent of iᵗʰ vertex
#cost is cost matrix where cost[i,j] denotes the cost of edge (i,j)

#Initialize single source arrays
for i=1 to n do
    d[i]= ∞
    π[i]= Null
s= Φ    #set of visited nodes
q=(1:n) #set of unvisited nodes
d[0]=0
while q!= Φ do
    u=EXTRACT_MIN(d) #Get the node with shortest distance
    s=s U {u}
    q=q \ {u}
    for each vertex v ∈ cost[u] do
        if d[v]> v.d + d[u] then  #v.d is distance of v from u
            d[v]=v.d + d[u]
            π[v]=u

"""

edges=list(map(str, input("Enter the edges : ").split()))
n=len(edges)
cost=list()
print("\nEnter the cost matrix :")
for _ in range(n):
    arr=list(map(str, input().split()))
    for i in range(n):
        if arr[i]=="None":
            arr[i]=None
        else:
            arr[i]=int(arr[i])
    cost.append(arr)
start=1
parent=[]
distances=[]
for _ in range(n):
    parent.append(None)
    distances.append(float('inf'))
distances[start-1]=0

def ShortestDistance(n,cost,visited,unvisited,distances,parent):
    minimum=float('inf')
    node=visited[-1]
    edge=[]
    for i in range(n):
        if i+1 not in visited and cost[node-1][i]!=None:
            parent[i]=edges[node-1]
            if cost[node-1][i]+distances[node-1]<distances[i]:
                if cost[node-1][i]+distances[node-1]<minimum:
                    edge=[node,i+1]
                    minimum=cost[node-1][i]+distances[node-1]
                distances[i]=cost[node-1][i]+distances[node-1]
    if len(edge)==0:
        minimum=float('inf')
        for i in range(n):
            if i+1 not in visited:
                if distances[i]<minimum:
                    node=i+1
                    minimum=distances[i]
        visited.append(node)
        unvisited.remove(node)
    else:
        visited.append(edge[1])
        unvisited.remove(edge[1])

def ShortestPath(n,source,cost,distances,parent):
    visited=[]
    unvisited=[1,2,3,4,5]
    visited.append(source)
    unvisited.remove(source)
    while len(unvisited)>0:
        ShortestDistance(n,cost,visited,unvisited,distances,parent)

ShortestPath(n,start,cost,distances,parent)
print("\nDistances : ")
for i in range(n):
    print(f"Distance to node {edges[i]} is {distances[i]}")

print("\nPath : ")
for i in range(n):
    if parent[i]!=None:
        print(f"Path to node {edges[i]} is : ",end="")
        path=list()
        path.append(edges[i])
        path.append(" → ")
        curr=parent[i]
        while curr!=None:
            path.append(curr)
            path.append(" → ")
            curr=parent[edges.index(curr)]
        del path[-1]
        print(*path[::-1])