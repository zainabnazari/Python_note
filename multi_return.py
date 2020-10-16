#file name: multi_return.py

def smallest_element(list_of_things):
    """
    Takes a list of comparable items. Returns the position of the smallest element and its value.
    """
    smallest_index = 0
    smallest_value = list_of_things[0]
    for index, element in enumerate(list_of_things):
        if element < smallest_value:
            smallest_value = element
            smallest_index = index
    return (smallest_index, smallest_value)
    
if __name__=="__main__":
    """The following test code is run only if the file is run, not if it is imported:"""
    small = smallest_element([9,3,1,4,2,8,4,6,2,6,2,5,72,1,76,8,-1,3,1000])
    print(small)
    print(small[0])
    print(small[1])
    
"""
output:
(16, -1)
16
-1
"""