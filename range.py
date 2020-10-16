# file name: range.py
print('this is the range of a given number 10')
x=range(10)
for n in x:
    print(n)
print('this is the range of given starting number 1, and ending number 10')
y=range(1,10)
for n in y:
    print(n)
print('this is the range of given starting number 1, and ending number 10,  with defined step=2')
z=range(1,10,2)
for n in z:
    print(n)
'''
output:
this is the range of a given number 10
0
1
2
3
4
5
6
7
8
9
this is the range of given starting number 1, and ending number 10
1
2
3
4
5
6
7
8
9
this is the range of given starting number 1, and ending number 10,  with defined step=2
1
3
5
7
9
'''
