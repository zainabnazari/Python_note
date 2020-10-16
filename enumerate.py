# file name: enumerate.py
# this is an example on how enumerate function works
mylist=['rose', 'orchid', 'tulip', 'sunflower']
for counter, value in enumerate(mylist, 1): # this 1 is to enumerate from one instead of zero.
    print(counter, value)

'''
output:
1 rose
2 orchid
3 tulip
4 sunflower

'''
