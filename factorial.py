# file name: factorail.py
# this code compute the factorail of a given number
a=input("what is your number? ")
b=1
c=1
while b<int(a):
    c=c*(b+1)
    b=b+1
print(c)
