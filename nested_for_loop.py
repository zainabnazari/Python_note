# file name: nested_for_loop.py

firstList = [2,3]
secondList = [4,5,6]
for i in firstList:
    for j in secondList:
        print("(",i,",",j,")")

"""
the output:
( 2 , 4 )
( 2 , 5 )
( 2 , 6 )
( 3 , 4 )
( 3 , 5 )
( 3 , 6 )
"""
