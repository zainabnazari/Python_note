#file name: copy_list.py
x=[1,2,3,4,5]
print("primary list x= ", x)
y=x # copying the refernce x to y!
print("y=", y)
y[0]=0 # making a change to y
print("changed y=", y)
print("after changing y, x=", x)

print("proper way of copying the elements of a list:")

y=list(x) # proper way of copying the elements of a list (way_1)
y=x[:] # proper way of copying the elements of a list (way_2)
print("primary list x= ", x)
# now let's check!
y[0]=-1
print("after changing y, x=", x)
print("after changing y, y=", y)

"""
output:
primary list x=  [1, 2, 3, 4, 5]
y= [1, 2, 3, 4, 5]
changed y= [0, 2, 3, 4, 5]
after changing y, x= [0, 2, 3, 4, 5]
proper way of copying the elements of a list:
primary list x=  [0, 2, 3, 4, 5]
after changing y, x= [0, 2, 3, 4, 5]
after changing y, y= [-1, 2, 3, 4, 5]

"""
