#file name: set.py
l = [4,2,6,1,"Carl",2]
print(l)
s = set(l)
print(s)
print("Zainab" in s)
print(2 in s)
print(2 in l)
#We can more easily make a set from scratch, without making a list first, using curly brackets:
s1 = {4,2,5,1,4,3}
print(s1)
"""
output:
[4, 2, 6, 1, 'Carl', 2]
{1, 2, 4, 6, 'Carl'}
False
True
True
{1, 2, 3, 4, 5}
"""