def minmax(arr,low,high):
    if high-low<=1:
        return(min(arr[low],arr[high]),max(arr[low],arr[high]))
    mid=(low+high)//2
    min1,max1=minmax(arr,low,mid)
    min2,max2=minmax(arr,mid+1,high)
    return min(min1,min2),max(max1,max2)

arr=[3,4,1,5,2]
print(minmax(arr,0,len(arr)-1))

# 3 4 1 5 2
# \____ min,max(arr,0,2) --> this will return (1,4)
#       \____ min,max(arr,0,1) : return (3,4)
#       \____ min,max(arr,2,2) : return (1,1)
#       \____ (1,4)
# \____ minmax(arr,3,4) --> this will return (2,5)
# \____(1,5)
