#file_name: kwargs.py
def test(parameter):
	print(parameter)
	
test(4)
test([1,2,3])

def test1(**kwargs):
	print(kwargs)
	
test1(blue=3,green=8, red="Carl", pink=[4,2,3,1])
"""
output:
4
[1, 2, 3]
{'blue': 3, 'green': 8, 'red': 'Carl', 'pink': [4, 2, 3, 1]}
"""