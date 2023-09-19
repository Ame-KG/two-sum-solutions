# in this solution we use the values as the keys instead of the indexes as the keys
# so we check if the value is in the dictionary then return the index
# else we insert the new value index pair
arr = [-3, 4, 3, 90]
target = 0


def twoSum(arr, target):
	dic = {}

	for i,n in enumerate(arr):
		diff = target - n
		if diff in dic:
			return (dic[diff], i)
		dic[n] = i



print(twoSum(arr, target))
		