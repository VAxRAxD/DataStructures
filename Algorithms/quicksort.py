def partition(arr,low,high):
    pivot=low
    pos=low
    for i in range(pos+1,high+1):
        if arr[i]<=arr[pivot]:
            pos+=1
            arr[i],arr[pos]=arr[pos],arr[i]
    arr[pos],arr[pivot]=arr[pivot],arr[pos]
    return pos

def quicksort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

arr=[10,7,8,19,1,5]
quicksort(arr,0,len(arr)-1)
print(arr)