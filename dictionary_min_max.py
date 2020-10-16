#file name: dictionary_min_max.py
ages={"Egypt": 5000, "Carl": 27, "Zainab": 31, "Albert Einstein": 141, "China": 5000}
print(min(ages))#first key in alphabetical order
print(max(ages))#last key in alphabetical order
print(sorted(ages))#sorts keys alphabetically
print(min(ages, key=ages.get))#key where the value is minimum.
print(max(ages, key=ages.get))#It returns the first key with the maximum value.
print(sorted(ages, key=ages.get))#list of keys, sorted by their values.
"""
output:
Albert Einstein
Zainab
['Albert Einstein', 'Carl', 'China', 'Egypt', 'Zainab']
Carl
Egypt
['Carl', 'Zainab', 'Albert Einstein', 'Egypt', 'China']
"""