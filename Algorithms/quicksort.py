count=0

def partition(arr,low,high):
    global count
    pivot=low
    pos=low
    for i in range(pos+1,high+1):
        if arr[i]<=arr[pivot]:
            pos+=1
            arr[i],arr[pos]=arr[pos],arr[i]
    arr[pos],arr[pivot]=arr[pivot],arr[pos]
    count+=1
    return pos

def quicksort(arr,low,high):
    if len(arr)==1:
        return arr
    if low<high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

arr=[10,7,8,19,1,5]
quicksort(arr,0,5)