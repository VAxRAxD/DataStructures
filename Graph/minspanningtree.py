cost=[[None,11,9,7,8],[11,None,15,14,13],[9,15,None,14,13],[7,14,12,None,6],[8,13,14,6,None]]

def distances(n,cost,visited):
    minimum=float('inf')
    for node in visited:
        for i in range(n):
            if i+1 not in visited:
                if cost[node-1][i]<minimum:
                    edge=[node,i+1]
                    minimum=cost[node-1][i]
    visited.append(edge[1])
    return minimum,edge

def minSpanningTree():
    visited=[]
    unvisited=[1,2,3,4,5]
    mincost=0
    edges=[]
    visited.append(unvisited[0])
    unvisited.remove(1)
    while len(unvisited) !=0:
        minimum,edge=distances(5,cost,visited)
        unvisited.remove(edge[1])
        mincost+=minimum
        edges.append(edge)
    print(mincost)
    print(edges)
minSpanningTree()