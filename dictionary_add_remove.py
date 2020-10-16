#file name: dictionary_add_remove.py
ages={"Egypt": 5000, "Carl": 27, "Zainab": 31, "Albert Einstein": 141, "China": 5000}
#print(dir(ages))
print(help(ages.update))
#ages.update("George":52)
print(ages)
"""
output:
Albert Einstein
Zainab
['Albert Einstein', 'Carl', 'China', 'Egypt', 'Zainab']
Carl
Egypt
['Carl', 'Zainab', 'Albert Einstein', 'Egypt', 'China']
"""