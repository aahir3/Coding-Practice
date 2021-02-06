def printRepeating(arr, n):
	mp = [0] * 100
	for i in range(0, n): 
		mp[arr[i]] += 1
    
	for i in range(0, n): 
		if (mp[arr[i]] > 1): 
			print(arr[i])
			mp[arr[i]] = 0
	

arr = [12, 10, 9, 45, 2, 10, 10, 45] 
n = len(arr) 
printRepeating(arr, n)