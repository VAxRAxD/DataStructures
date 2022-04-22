nodes=int(input("Enter the number of nodes : "))
adj=list()
print("Enter the adjacency matrix : ")
for _ in range(nodes):
    vertex=list(map(int,input().split()))
    adj.append(vertex)
colors=list()
n=int(input("Enter the number of colors : "))
for i in range(n):
    colors.append("C"+str(i+1))
x=[0 for _ in range(nodes)]

print("The solution vector is : ")
def coloring(c,nodes,adj,colors,x,k):
    if k==nodes:
        print(x)
    if k<nodes:
        available=colors.copy()
        for i in range(nodes):
            if adj[k][i]==1:
                if x[i] in available:
                    available.remove(x[i])
        for color in available:
            if k==0:
                x=[0 for _ in range(nodes)]
            x[k]=color
            coloring(color,nodes,adj,colors,x,k+1)

coloring("Null",nodes,adj,colors,x,0)
    