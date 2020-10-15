import time


class Selection_sort:
	def __init__(self, list_of_obj):
		self.list_of_obj = list_of_obj
		self.swap_quantity = 0
		self.compare_quantity = 0
		self.duration = 0


	def sort_by_width_desc(self):
		start_time = time.time()
		list_of_sofa = self.list_of_obj
		i = 0
		length = len(list_of_sofa)
		self.compare_quantity = length + 1
		while i < length:
			j = i +1
			max_idx = i
			self.compare_quantity += length - j + 1
			while j < length:
				self.compare_quantity += 1
				if list_of_sofa[max_idx].width < list_of_sofa[j].width:
					max_idx = j
				j+=1

			# self.compare_quantity += 1
			# if max_idx != i:
			# 	self.swap_quantity +=1
			# 	list_of_sofa[i], list_of_sofa[max_idx] = list_of_sofa[max_idx], list_of_sofa[i]
			
			list_of_sofa[i], list_of_sofa[max_idx] = list_of_sofa[max_idx], list_of_sofa[i]
			i +=1
		self.swap_quantity = length
		
		self.duration = time.time()-start_time
		print('name = selection sort by width desc')
		print('time = ' + str(self.duration))
		print('compare quantity = ' + str(self.compare_quantity))
		print('swap quantity = ' + str(self.swap_quantity))

		return list_of_sofa
