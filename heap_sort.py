import time


class Heap_sort:
	def __init__(self, list_of_obj):
		self.list_of_obj = list_of_obj
		self.compare_quantity = 0
		self.swap_quantity = 0
		self.duration = 0

	def max_heapify(self, list_of_sofa, length, idx):
		largest_idx = idx
		right_child_idx = idx * 2 + 2
		left_child_idx = idx * 2 + 1

		if right_child_idx < length and list_of_sofa[largest_idx].length < list_of_sofa[right_child_idx].length:
			largest_idx = right_child_idx

		if left_child_idx < length and list_of_sofa[largest_idx].length < list_of_sofa[left_child_idx].length:
			largest_idx = left_child_idx

		if largest_idx != idx:
			self.swap_quantity += 1
			list_of_sofa[largest_idx], list_of_sofa[idx] = list_of_sofa[idx], list_of_sofa[largest_idx]
			Heap_sort.max_heapify(self, list_of_sofa, length, largest_idx)
		self.compare_quantity += 3
	
	def heapsort_by_lenth_asc(self):
		start_time = time.time()
		list_of_sofa = self.list_of_obj
		length = len(list_of_sofa)		

		iterator = length // 2 - 1

		self.compare_quantity += iterator + 2
		while iterator >= 0:
			Heap_sort.max_heapify(self, list_of_sofa, length, iterator)
			iterator -= 1

		self.compare_quantity += 1
		while length > 1:
			self.swap_quantity += 1
			list_of_sofa[length-1], list_of_sofa[0] = list_of_sofa[0], list_of_sofa[length-1]
			length -= 1
			Heap_sort.max_heapify(self, list_of_sofa, length, 0)
			self.compare_quantity += 1
			
		self.duration = time.time()-start_time
		print('name = heap sort by length asc')
		print('time = ' + str(self.duration))
		print('compare quantity = ' + str(self.compare_quantity))
		print('swap quantity = ' + str(self.swap_quantity))

		return list_of_sofa
