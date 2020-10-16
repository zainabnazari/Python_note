#file name: multi_return.py

def smallest_element(list_of_things):
    """
    Takes a list of comparable items. Returns the position of the smallest element and its value.
    """
    val=3
    smallest_indices =[]
    the_value = val
    smallest_values=[]
    for index, element in enumerate(list_of_things):
        if element < the_value:
            smallest_values += [element]
            smallest_indices += [index]

    return (smallest_indices, smallest_values)

if __name__=="__main__":
    """The following test code is run only if the file is run, not if it is imported:"""
    smalls = smallest_element([9,3,1,4,2,8,4,6,2,6,2,5,72,1,76,8,-1,3,1000])

    print(smalls)
    print(smalls[0])
    print(smalls[1])

"""
output:
(16, -1)
16
-1
"""
