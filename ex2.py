# file name: ex2.py
s = 0
p = 1

while True:
    num = input('Number or q to quit: ')
    if num == 'q':
        break
    num = int(num)
    s += num
    p *= num
print('Sum:',s,'Product:',p)
