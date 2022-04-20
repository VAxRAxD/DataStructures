"""
ALGORITHM_PRIM
#cost is cost matrix where cost[i,j] denotes the cost of edge (i,j)

e= {} #Initialize empty set for storing all visited edges
s= Φ
q=(1,n)
s=s U {1}
q=q \ {1}
while q!=Φ do
    for each vertex v ∈ cost[e] do
        e=e U {(e,v)}
    u=EXTRACT_MIN(e) #Get edge with the minimum cost
    x= x U {u}
    e=e \ {u}
    s=s U {u.v}
    q=q \ {u.v}

"""
n=int(input("Enter the no. of edges: "))
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

def distances(n,cost,visited):
    minimum=float('inf')
    for node in visited:
        for i in range(n):
            if i+1 not in visited and cost[node-1][i]!=None:
                if cost[node-1][i]<minimum:
                    edge=[node,i+1]
                    minimum=cost[node-1][i]
    visited.append(edge[1])
    return minimum,edge

def minSpanningTree(n):
    visited=[]
    unvisited=[i+1 for i in range(n)]
    print(unvisited)
    mincost=0
    edges=[]
    visited.append(unvisited[0])
    unvisited.remove(1)
    while len(unvisited) !=0:
        minimum,edge=distances(n,cost,visited)
        unvisited.remove(edge[1])
        mincost+=minimum
        edges.append(edge+[mincost])
    print("\nThe edges in minimum spanning tree are :")
    for edge in edges:
        print(f"({edge[0]} {edge[1]}), Cost: {edge[2]}")
    print("\nThe cost if MST is ",mincost)
minSpanningTree(n)