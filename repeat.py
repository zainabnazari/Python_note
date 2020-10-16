# file name: repeat.py
'''
this code is going to be take a number and then type it something like
let's assume the given number is 5
then our code is going to print the result as follow
5
55
555
5555
55555
'''
b=input("what is your number? ")
c=1
while c<=int(b):
    print(b*c)
    c=c+1
