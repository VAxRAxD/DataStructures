"""
ALGORITHM_KRUSKAL
#cost is cost matrix where cost[i,j] denotes the cost of edge (i,j)
#n is the total number of nodes
#nodes={1..n} contains all the nodes

e= {} #Initialize empty set for storing all edges
x= {} #Initialize empty set for storing all edges of MST
for i=1 to n do
    for each vertex v ∈ cost[i] do
        e=e U {(i,v,,cost[s][v])}
e.SORT #Sort the edges on basis of their edge-cost
for each edge u ∈ e do
    if not CYCLE(u) then
        x= x U {u}
        e=e \ {u}

CYCLE(e)
#e is the edges where e[i,j,cost] denotes the soure node, destination node & its cost

if node[e[i]]==node[e[j]] then
    return TRUE
for each node i ∈ nodes do
    if i==node[e[j]] then
        i=node[e[i]]
return FALSE

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
def cycle(nodes,vertices):
    a,b,c=map(int,vertices)
    if nodes[a-1]==nodes[b-1]:
        return True
    nodes[:]=[x if x!=nodes[b-1] else nodes[a-1] for x in nodes]
    return False

def distances(n,cost):
    edges=[]
    for i in range(n):
        for j in range(n):
            if cost[i][j]!=None:
                edges.append([i+1,j+1,cost[i][j]])
    edges=sorted(edges,key=lambda x:x[2])
    return edges

def minSpanningTree(n,cost):
    mst=[]
    nodes=[i for i in range(n)]
    edges=distances(n,cost)
    for edge in edges:
        if not cycle(nodes,edge):
            mst.append(edge)
    cost=0
    print("\nThe edges in minimum spanning tree are :")
    for edge in mst:
        print(f"({edge[0]} {edge[1]}), Cost: {edge[2]}")
        cost+=edge[2]
    print(f"\nThe cost of MST is {cost}")

minSpanningTree(n,cost)