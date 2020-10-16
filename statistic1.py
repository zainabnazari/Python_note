#file name: statistic1.py
list1=["Carl", "Hanna", "Piter", "Ali", "Hassan", "Paul", "Zainab", "Zahra", "Catalina", "Anna", "Julia", "Dina", "Sara", "Lina", "Albert"]
list2=[1.80,1.67,1.87,1.55,1.77,1.56,1.78,1.69,1.80,1.58, 1.87, 1.59, 1.65, 1.90, 1.79]
import numpy as np
height_np=np.array(list2)
name_np=np.array(list1)
# let's figure out the height of Zahra and Julia:
print("Zahra height= ", height_np[name_np=="Zahra"], "Julia height= ", height_np[name_np=="Julia"])
'''
output
Zahra height=  [1.69] Julia height=  [1.87]
'''
