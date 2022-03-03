#Approach 1
arr=[14,33,27,10,35,19,42,44]
for i in range(len(arr)):
	small=arr[i]
	pos=i
	for j in range(i,len(arr)):
		if arr[j]<small:
			small=arr[j]
			pos=j
	arr[i],arr[pos]=arr[pos],arr[i]
print(*arr)
