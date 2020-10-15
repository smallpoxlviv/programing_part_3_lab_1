import csv
import random
import string
from sofa import Sofa
from selection_sort import Selection_sort
from heap_sort import Heap_sort

if __name__ == '__main__':
	
	with open('sofas.csv') as file:
		reader = csv.reader(file)
		list_for_sofa = list(reader)

	list_of_sofa = []
	for sofa in list_for_sofa:
		list_of_sofa.append(Sofa(sofa[0],sofa[1],sofa[2],sofa[3]))

	selection_sort = Selection_sort(list_of_sofa)
	selection_sorted = selection_sort.sort_by_width_desc()

	for el in selection_sorted:
		print(el)

	print('')
	heap_sort = Heap_sort(list_of_sofa)
	heap_sorted = heap_sort.heapsort_by_lenth_asc()

	for el in heap_sorted:
		print(el)

