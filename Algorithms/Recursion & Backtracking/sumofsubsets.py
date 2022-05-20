"""
ALGORITHM_SUM_OF_SUBSETS(s,r,k,m)
#arr[1:n] contains the set of numbers
#m is the maximum sun
#x{1..n} is the solution vector

s=0 #To store the sum obtained
k=0
r=SUM(arr) #To store the remaining weight
if s==m then
    PRINT x
if k < n then
    / Left Tree /
    if s+arr[k]<=m then
        x[k]=1
        ALGORITHM_SUM_OF_SUBSETS(s+arr[k],r-arr[k],k+1,m)
    / Right Tree /
    x[k]=0
    if s+arr[k+1]<=m and s+r-arr[k]>=m then
        ALGORITHM_SUM_OF_SUBSETS(s,r-arr[k],k+1,m)

"""

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