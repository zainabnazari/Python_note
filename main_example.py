# file name: main_example.py
# this is the second file which is importing the main_file, the first file
from main_file import Person

professor = Person()
professor.function("Mehran", 45)

print(professor.name)
"""
When we run this file, the output is:
"Mehran"
"""
