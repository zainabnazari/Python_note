# file name: Init.py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)#The __init__ function allows us to specify parameters for the instantiation of p1.
print(p1.name)
print(p1.age)
