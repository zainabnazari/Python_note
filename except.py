#file name:except.py
list=[1,3,55,0,9,88,20,50,0,24,44,76,100]
for i in list:
    try:
       print(30/i)
    except ZeroDivisionError:
       print("Oh, that's bad!")
'''
output:

30.0
10.0
0.5454545454545454
Oh, that's bad!
3.3333333333333335
0.3409090909090909
1.5
0.6
Oh, that's bad!
1.25
0.6818181818181818
0.39473684210526316
0.3

'''
