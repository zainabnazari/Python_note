#file name: list.py
my_list=[1,2,4.4, 7, ["carl", 27]]
#
print("my_list: \n", my_list)
print("my_list[3]: \n", my_list[3])

# deleting an element in the list:

del(my_list[3])
print("my_list after deleting my_list[3]:\n ", my_list)

# accessing the list in the list:
print("my_list[-1][:]: \n", my_list[-1][:])

#replacing element:
my_list[0]="zainab"
print("my_list after replacing my_list[0]=\"zainab\":\n ", my_list)
'''
output:

my_list:
 [1, 2, 4.4, 7, ['carl', 27]]
my_list[3]:
 7
my_list after deleting my_list[3]:
  [1, 2, 4.4, ['carl', 27]]
my_list[-1][:]:
 ['carl', 27]
my_list after replacing my_list[0]="zainab":
  ['zainab', 2, 4.4, ['carl', 27]]

  '''
