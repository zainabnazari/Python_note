#file name: carl_test.py
bb=[3,-7,3]
for index, element in enumerate(bb):
	if element < 0 and index > 0 and index < len(bb) - 1:
		filtered_value = (bb[index] + bb[index - 1] + bb[index + 1]) / 3
		bb[index] = filtered_value
		bb[index - 1] = filtered_value
		bb[index + 1] = filtered_value
	elif element < 0 and index > 0:
		filtered_value = (bb[index] + bb[index - 1]) / 2
		bb[index] = filtered_value
		bb[index - 1] = filtered_value
	elif element < 0 and index < len(bb) - 1:
		filtered_value = (bb[index] + bb[index + 1]) / 2
		bb[index] = filtered_value
		bb[index + 1] = filtered_value
		
print(bb)