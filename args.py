#file_name: args.py
def test(parameter):
	print(parameter)
	
test(4)
test([1,2,3])

def test1(*args):
	print(args)
	
test1(3,8, "Carl", [4,2,3,1])
"""
output:
4
[1, 2, 3]
(3, 8, 'Carl', [4, 2, 3, 1])
"""