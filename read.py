# file name: read.py
# here is the code to read data into our file
f=open("data.csv", "r")
contents=f.read()
myarray=eval(contents)
for n in myarray:
    print(n*2)
#print(myarray*2, type(myarray))
