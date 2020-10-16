#file name: dictionary_iteration.py
ages={"Egypt": 5000, "Carl": 27, "Zainab": 31, "Albert Einstein": 141, "China": 5000}
print("keys:")
for item in ages:
	print(item)
	
print("values:")
for item in ages:
	print(ages[item])
"""
output:
keys:
Egypt
Carl
Zainab
Albert Einstein
China
values:
5000
27
31
141
5000
"""