arr=list(map(int,input("Enter the numbers : ").split()))
m=int(input("Enter the maximum sum : "))
x=[0 for _ in range(len(arr))]

print("The solution vector is : ",end=" ")
def sums(s,r,k,m,x):
    if s==m:
        print(x,end=" ")
    if k<len(arr):
        """Left Tree"""
        if s+arr[k]<=m:
            x[k]=1
            sums(s+arr[k],r-arr[k],k+1,m,x)
        """Right Tree"""
        x[k]=0
        try:
            if s+arr[k+1]<=m and s+r-arr[k]>=m:
                sums(s,r-arr[k],k+1,m,x)
        except:
            pass

sums(0,sum(arr),0,m,x)