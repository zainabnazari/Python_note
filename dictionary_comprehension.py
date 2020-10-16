#file name: dictionary_comprehension.py
radius=[1,2,3,4,5]
radiusToArea = {r:(r**2)*3.14 for r in radius}#This is a dictionary with radii of circles as keys and areas as values.
print(radiusToArea)
"""
output:
{1: 3.14, 2: 12.56, 3: 28.26, 4: 50.24, 5: 78.5}
"""