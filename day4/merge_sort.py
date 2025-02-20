def merge_sort(numbers, low, high):
	if low < high:
		mid = (low + (high - low) // 2)
		#mid = (low + high) // 2
		merge_sort(numbers, low, mid-1)
		merge_sort(numbers, mid, high)
		merge(numbers, low, mid, high)

# while i < len(array1) and j < len(array2):
	
def merge(numbers, low, mid, high):
	array1
	
	
	merged_array = []
	k = low
	i = 0
	j = 0
	while 
		if array1[i] < array2[j]:
			merged_array[k] =  array1[i]
			i += 1
		else:
			merged_array[k] =  array1[j]
			j += 1
		k += 1
	merged_array += array1[i:]
	merged_array += array1[j:]
