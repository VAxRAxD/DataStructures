#Approach 1
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    return merge_two_sorted_lists(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def sort(arr):
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            return
        else:
            arr[i],arr[i + 1]=arr[i+1],arr[i]

def merge_two_sorted_lists(left,right):
    for i in range(len(left)):
        if left[i]>right[0]:
            left[i],right[0]=right[0],left[i]
            sort(right)
    return left+right

arr = [10,3,15,7,8,23,98,29]
print(merge_sort(arr))

#Approach 2
def merge_sort(arr,left,right):
    if left>=right:
        return
    mid = (left+right+1)//2
    merge_sort(arr,left,mid-1)
    merge_sort(arr,mid,right)
    merge_two_sorted_lists(arr,left,mid,right)

def sort(arr,mid,right):
    for i in range(mid,right):
        if arr[i]<=arr[i+1]:
            return
        else:
            arr[i],arr[i + 1]=arr[i+1],arr[i]

def merge_two_sorted_lists(arr,left,mid,right):
    for i in range(left,mid):
        if arr[i]>arr[mid:right+1][0]:
            arr[i],arr[mid]=arr[mid],arr[i]
            sort(arr,mid,right)
    print(arr)

arr = [9,8,7,6,5,4,3,2]
merge_sort(arr,0,len(arr)-1)
