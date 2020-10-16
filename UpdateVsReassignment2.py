#file name: UpdateVsReassignment2.py

a = [1,2,3]
b = a#b and a now refer to the same list...
print("***Update***")
a += [4,5]#...so any changes to one of them affect both
print("a=",a)#[1, 2, 3, 4, 5]
print("b=",b)#[1, 2, 3, 4, 5]

print("***Assignment***")
a = a + [6,7]#This is a reassignment. A new list is assigned to the variable a. So a and b are no longer the same list.
print("a=",a)#[1, 2, 3, 4, 5, 6, 7]
print("b=",b)#[1, 2, 3, 4, 5]
"""
output:
***Update***
a= [1, 2, 3, 4, 5]
b= [1, 2, 3, 4, 5]
***Assignment***
a= [1, 2, 3, 4, 5, 6, 7]
b= [1, 2, 3, 4, 5]

"""