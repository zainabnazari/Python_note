# file name: write.py
'''
here is a simple example to show how we can open a file and write into it the data  that in this case, it is an array of 5 digits,  however, the write file can only accept strings, therfore we need to convert the integeres to strings.
'''

x=[1,2,3,4,5]
file=open('data.csv','w') # here 'w' means write, note that it also it works with .dat, and .txt format
file.write(str(x))
'''
output in the file:
[1 2 3 4 5]

'''
# Note, if data.txt already exists, then if you run the code, the content of the data.txt is going to be replaced.
