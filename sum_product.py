#file name=sum_product.py
# this code can take numbers (as mush as you give- if not enter the letter 'q' to exit )
# and print the sum and product of them.

s = 0
p = 1

while True: #This is just a regular while loop, but the condition always stays true. The loop will continue indefinitely...
    num = input('Number or q to quit: ')
    if num == 'q':
        break #...unless it is broken using the "break"-command. The "break"-command ends the while loop.
    num = int(num)
    s += num
    p *= num
print('Sum:',s,'Product:',p)
