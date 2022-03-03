#Approach 1
arr=[40,10,50,30,20]
for i in range(1,len(arr)):
	while i>0:
		if arr[i]<arr[i-1]:
			arr[i],arr[i-1]=arr[i-1],arr[i]
		else:
			break
		i-=1
print(*arr)


#Approach 2
arr=[40,10,50,30,20]
for i in range(1,len(arr)):
	key=arr[i]
	j=i-1
	while j>=0 and arr[j]>key:
		arr[j+1]=arr[j]
		j-=1
	arr[j+1]=key
print(*arr)