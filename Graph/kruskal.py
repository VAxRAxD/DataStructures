cost=[[None,28,None,None,None,10,None],[None,None,16,None,None,None,14],[None,None,None,12,None,None,None],[None,None,None,None,None,None,18],[None,None,None,22,None,None,None],[None,None,None,None,25,None,None],[None,None,None,None,24,None,None]]
n=7
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
    nodes=[1,2,3,4,5,6,7]
    edges=distances(n,cost)
    for edge in edges:
        if not cycle(nodes,edge):
            mst.append(edge)
    cost=0
    for edge in mst:
        print([edge[0],edge[1]],end=" ")
        cost+=edge[2]
    print(f"\n{cost}")

minSpanningTree(n,cost)