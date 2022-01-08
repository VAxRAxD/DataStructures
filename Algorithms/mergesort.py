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

if __name__ == '__main__':
    arr = [10,3,15,7,8,23,98,29]
    print(merge_sort(arr))