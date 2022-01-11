arr=[40,10,50,30,20]
for i in range(1,len(arr)):
	while i>0:
		if arr[i]<arr[i-1]:
			arr[i],arr[i-1]=arr[i-1],arr[i]
		else:
			break
		i-=1
print(*arr)