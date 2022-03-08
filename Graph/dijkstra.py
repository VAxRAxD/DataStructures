cost=[[None,10,3,None,None],[None,None,1,2,None],[None,4,None,8,2],[None,None,None,None,7],[None,None,None,None,9]]
start=1
n=5
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
            parent[i]=node
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
print(distances)
print(parent)