w=int(input("Enter the maximum weight: "))
n=int(input("Enter the number of items: "))
weights=list(map(int,input("Enter the weights of items: ").split()))
values=list(map(int,input("Enter the values of items: ").split()))
matrix=[[ 0 for _ in range(w+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,w+1):
        rem=j
        curr=i-1
        total=0
        while curr>=0:
            if weights[curr]<=rem:
                total+=values[curr]
                rem-=weights[curr]
            curr-=1
        if total!=0:
            if total<matrix[i-1][j]:
                matrix[i][j]=matrix[i-1][j]
            else:
                matrix[i][j]=total
        else:
            matrix[i][j]=matrix[i-1][j]

print("\nThe matrix is : ")
for row in matrix:
    print(*row)

rem=w
item=n
arr=list()
while rem>0:
    if matrix[item][rem]!=matrix[item-1][rem]:
        arr.append(item)
        rem-=weights[item-1]
    item-=1

print("\nThe solution is { ",end="")
for i in range(1,n+1):
    if i in arr:
        print("1",end=" ")
    else:
        print("0",end=" ")
print("}")
