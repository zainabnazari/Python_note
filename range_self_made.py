#file name: range_self_made
def range_self_made(start, end):
    while start < end:
        yield(start)
        start = start + 1
        
for i in range_self_made(4,9):
    print(i)
    
"""
output:
4
5
6
7
8
"""