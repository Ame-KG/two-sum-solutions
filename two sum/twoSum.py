# in this solution we use a hashmap do store  the values of the list and their index and then another loop to traverse it
# this fails to take advantage of hashmaps and could have been acheived by just using a single array
# this gives a complexity of O(n^2) in the worst case scenario


arr = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17]
target = 12
dic = {}
for i, n in enumerate(arr):
	if n == target:
		print(f'{n} = target')

	else:
		dic[i] = n
		for l in range(i):

			if n + dic[l] == target:
				print(f'{n} + {dic[l]} == target')
				exit()
		