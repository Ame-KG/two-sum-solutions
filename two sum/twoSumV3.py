# in this solution, we insert everything into the dictionary
# however we do not use a second loop to search the dictionary
# instead we get the difference between n and the target and check if the difference is in the dictionary already with index()
# we convert the keys into a list and the values into a list
# if not we move on to the next n value and repeat until we arrive at an n in which the difference is already in the dict
# at the worst case this gives O(n)
# in this iteragtion we try to decrease the

arr = [-3, 4, 3, 90]
target = 0


def twoSum(arr, target):
	dic = {}
	
	for i,n in enumerate(arr):
		dic[i] = n
		diff = target - n
		vals = list(dic.values())
		if diff in vals:
			position = vals.index(diff)
			# print(f'differenc: {diff}, n: {n}, target: {target}, key:{keys[position]}, i: {i}')
			if list(dic.keys()).index(position) != i:
				return(list(dic.keys()).index(position), i)



print(twoSum(arr, target))