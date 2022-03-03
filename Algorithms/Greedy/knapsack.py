n=int(input("Enter the number of items : "))
values=list(map(int,input("Enter the values of the items: ").split()))
weights=list(map(int,input("Enter the weight of the items: ").split()))
capacity=int(input("Enter the maximum capacity : "))
items=list()
for i in range(n):
    dict={}
    dict['Number']=i+1
    dict['Value']=values[i]
    dict['Weight']=weights[i]
    items.append(dict)
items=sorted(items, key = lambda x : x['Value']/x['Weight'],reverse=True)
remaining=capacity
total=0
selected=[0 for _ in range(n)]
i=0
while i<n:
    if items[i]['Weight']>remaining:
        break
    remaining-=items[i]['Weight']
    total+=items[i]['Value']
    selected[items[i]['Number']-1]=1
    i+=1
if i<=n-1 and remaining!=0:
    total+=(items[i]['Value'])/(items[i]['Weight']/remaining)
    selected[items[i]['Number']-1]=float("{0:.2f}".format(remaining/items[i]['Weight'] ))
print(total)
print(selected)