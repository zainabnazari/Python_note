#file name: zip_example.py
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']
l=list(zip(number_list, str_list))
print(l)
"""
output:
[(1, 'one'), (2, 'two'), (3, 'three')]
"""
#Why is this useful?:
#Assume we want to have a dictionary like this:
#{1:"one", 2:"two", 3:"three"}
print({i[0]:i[1] for i in zip(number_list, str_list)})
"""
output:
{1: 'one', 2: 'two', 3: 'three'}
"""