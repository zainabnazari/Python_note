#file name: list_comprehension.py
#old way:
newList = []
oldList = [1,2,3]
for i in oldList:
	newList += [i/2]
#new way:
newList2 = [i/2 for i in oldList]
print("old way:", newList)
print("new way:", newList2)
"""
output:
[0.5, 1.0, 1.5]
[0.5, 1.0, 1.5]
"""